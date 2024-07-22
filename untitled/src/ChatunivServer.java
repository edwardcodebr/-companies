import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.HashMap;
import java.util.Map;

public class ChatunivServer {
    private static Map<String, User> users = new HashMap<>();
    private static Map<String, ClientHandler> clients = new HashMap<>();

    public static void main(String[] args) {
        System.out.println("O servidor Chatuniv está rodando...");
        try (ServerSocket listener = new ServerSocket(20041)) {
            while (true) {
                new ClientHandler(listener.accept()).start();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static class User {
        private String username;
        private String password;

        public User(String username, String password) {
            this.username = username;
            this.password = password;
        }

        public String getUsername() {
            return username;
        }

        public String getPassword() {
            return password;
        }

        public void setUsername(String username) {
            this.username = username;
        }

        public void setPassword(String password) {
            this.password = password;
        }
    }

    private static class ClientHandler extends Thread {
        private Socket socket;
        private PrintWriter out;
        private BufferedReader in;
        private String username;

        public ClientHandler(Socket socket) {
            this.socket = socket;
        }

        public void run() {
            try {
                in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                out = new PrintWriter(socket.getOutputStream(), true);

                // Autenticação
                while (true) {
                    String line = in.readLine();
                    if (line.startsWith("REGISTER")) {
                        String[] parts = line.split(" ");
                        String username = parts[1];
                        String password = parts[2];
                        synchronized (users) {
                            if (!users.containsKey(username)) {
                                users.put(username, new User(username, password));
                                out.println("REGISTRATION_SUCCESS");
                            } else {
                                out.println("REGISTRATION_FAILED");
                            }
                        }
                    } else if (line.startsWith("LOGIN")) {
                        String[] parts = line.split(" ");
                        String username = parts[1];
                        String password = parts[2];
                        synchronized (users) {
                            User user = users.get(username);
                            if (user != null && user.getPassword().equals(password)) {
                                this.username = username;
                                clients.put(username, this);
                                out.println("NAMEACCEPTED");
                                break;
                            } else {
                                out.println("LOGIN_FAILED");
                            }
                        }
                    }
                }

                String message;
                while ((message = in.readLine()) != null) {
                    if (message.startsWith("/logout")) {
                        break;
                    } else if (message.startsWith("/list")) {
                        listUsers();
                    } else if (message.startsWith("@")) {
                        String[] parts = message.split(" ", 2);
                        if (parts.length == 2) {
                            String targetUsername = parts[0].substring(1);
                            String privateMessage = parts[1];
                            sendMessageToUser(targetUsername, "Mensagem privada de " + username + ": " + privateMessage);
                        }
                    } else if (message.startsWith("/changepass")) {
                        String newPassword = message.split(" ")[1];
                        changePassword(newPassword);
                    } else {
                        broadcastMessage(username + ": " + message);
                    }
                }
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                try {
                    socket.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
                synchronized (clients) {
                    clients.remove(username);
                }
                System.out.println("User " + username + " saiu do chat");  // Log de saída no terminal
                broadcastMessage("User " + username + " saiu do chat");
            }
        }

        private void broadcastMessage(String message) {
            synchronized (clients) {
                for (ClientHandler handler : clients.values()) {
                    handler.out.println(message);
                }
            }
        }

        private void sendMessageToUser(String username, String message) {
            synchronized (clients) {
                ClientHandler handler = clients.get(username);
                if (handler != null) {
                    handler.out.println(message);
                } else {
                    out.println("Usuário " + username + " não está disponível.");
                }
            }
        }

        private void listUsers() {
            synchronized (clients) {
                StringBuilder userList = new StringBuilder("Usuários online: ");
                for (String user : clients.keySet()) {
                    userList.append(user).append(", ");
                }
                out.println(userList.substring(0, userList.length() - 2)); // Remover a última vírgula e espaço
            }
        }

        private void changePassword(String newPassword) {
            synchronized (users) {
                User user = users.get(username);
                if (user != null) {
                    user.setPassword(newPassword);
                    out.println("Senha alterada com sucesso.");
                }
            }
        }
    }
}
