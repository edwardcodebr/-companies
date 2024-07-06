import javax.swing.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class ChatunivClient {
    private BufferedReader in;
    private PrintWriter out;
    private JFrame frame = new JFrame("Chatuniv Cliente");
    private JTextArea chatArea = new JTextArea(20, 50);
    private JTextField textField = new JTextField(50);
    private String username;

    public ChatunivClient() {
        // Interface do usuário
        chatArea.setEditable(false);
        frame.getContentPane().add(new JScrollPane(chatArea), "Center");
        frame.getContentPane().add(textField, "South");
        frame.pack();

        // Nome de usuário
        username = JOptionPane.showInputDialog(frame, "Digite seu nome:");
        frame.setTitle("Chatuniv Cliente - " + username);

        // Configuração da conexão com o servidor
        try {
            Socket socket = new Socket("localhost", 20041); // Conexão local, ajuste conforme necessário
            in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            out = new PrintWriter(socket.getOutputStream(), true);

            // Envio do nome de usuário ao servidor
            out.println(username);

            // Thread para receber mensagens do servidor
            new Thread(() -> {
                try {
                    while (true) {
                        String line = in.readLine();
                        if (line.startsWith("NAMEACCEPTED")) {
                            textField.setEditable(true);
                        } else {
                            chatArea.append(line + "\n");
                        }
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }).start();

            // Enviar mensagem ao pressionar Enter
            textField.addActionListener(e -> {
                out.println(textField.getText());
                textField.setText("");
            });

            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setVisible(true);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(ChatunivClient::new);
    }
}
