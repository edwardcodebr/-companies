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

        // Tela de login/registro
        showLoginMenu();

        // Thread para receber mensagens do servidor
        new Thread(() -> {
            try {
                while (true) {
                    String line = in.readLine();
                    if (line != null) {
                        chatArea.append(line + "\n");
                    }
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }).start();

        // Enviar mensagem ao pressionar Enter
        textField.addActionListener(e -> {
            String text = textField.getText();
            if ("/back".equalsIgnoreCase(text.trim())) {
                showOptionsMenu();
            } else {
                out.println(text);
            }
            textField.setText("");
        });

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }

    private void showLoginMenu() {
        while (true) {
            String[] options = {"Login", "Registrar"};
            int choice = JOptionPane.showOptionDialog(frame, "Escolha uma opção:", "Login/Registrar", JOptionPane.DEFAULT_OPTION, JOptionPane.INFORMATION_MESSAGE, null, options, options[0]);

            if (choice == 0) { // Login
                username = JOptionPane.showInputDialog(frame, "Digite seu nome:");
                String password = JOptionPane.showInputDialog(frame, "Digite sua senha:");

                if (username != null && password != null) {
                    // Configuração da conexão com o servidor
                    try {
                        Socket socket = new Socket("localhost", 20041); // Conexão local, ajuste conforme necessário
                        in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                        out = new PrintWriter(socket.getOutputStream(), true);

                        // Envio do nome de usuário e senha ao servidor
                        out.println("LOGIN " + username + " " + password);

                        String response = in.readLine();
                        if ("NAMEACCEPTED".equals(response)) {
                            frame.setTitle("Chatuniv Cliente - " + username);
                            showOptionsMenu();
                            break;
                        } else {
                            JOptionPane.showMessageDialog(frame, "Nome de usuário ou senha incorretos.", "Erro", JOptionPane.ERROR_MESSAGE);
                        }
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }
            } else if (choice == 1) { // Registrar
                username = JOptionPane.showInputDialog(frame, "Digite seu nome:");
                String password = JOptionPane.showInputDialog(frame, "Digite sua senha (4 dígitos):");

                if (username != null && password != null && password.length() == 4) {
                    // Configuração da conexão com o servidor
                    try {
                        Socket socket = new Socket("localhost", 20041); // Conexão local, ajuste conforme necessário
                        in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                        out = new PrintWriter(socket.getOutputStream(), true);

                        // Envio do nome de usuário e senha ao servidor
                        out.println("REGISTER " + username + " " + password);

                        String response = in.readLine();
                        if ("REGISTRATION_SUCCESS".equals(response)) {
                            JOptionPane.showMessageDialog(frame, "Registrado com sucesso! Faça login.", "Sucesso", JOptionPane.INFORMATION_MESSAGE);
                        } else {
                            JOptionPane.showMessageDialog(frame, "Nome de usuário já existe.", "Erro", JOptionPane.ERROR_MESSAGE);
                        }
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                } else {
                    JOptionPane.showMessageDialog(frame, "A senha deve ter 4 dígitos.", "Erro", JOptionPane.ERROR_MESSAGE);
                }
            }
        }
    }

    private void showOptionsMenu() {
        String[] options = {"Enviar mensagem", "Mudar senha", "Logout"};
        while (true) {
            int choice = JOptionPane.showOptionDialog(frame, "Escolha uma opção:", "Menu de Opções", JOptionPane.DEFAULT_OPTION, JOptionPane.INFORMATION_MESSAGE, null, options, options[0]);
            if (choice == 0) {
                break; // Enviar mensagem
            } else if (choice == 1) {
                String newPassword = JOptionPane.showInputDialog(frame, "Digite a nova senha (4 dígitos):");
                if (newPassword != null && newPassword.length() == 4) {
                    out.println("/changepass " + newPassword);
                } else {
                    JOptionPane.showMessageDialog(frame, "A senha deve ter 4 dígitos.", "Erro", JOptionPane.ERROR_MESSAGE);
                }
            } else if (choice == 2) {
                out.println("/logout");
                showLoginMenu();
                break;
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(ChatunivClient::new);
    }
}
