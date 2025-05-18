import socket
import threading

# Server Configuration
HOST = '172.20.10.6'
PORT = 12345

clients = {}  # Dictionary to store clients: {username: socket}

def broadcast(message, sender_socket=None):
    """Send a message to all clients except the sender."""
    for client_socket in clients.values():
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode())
            except:
                client_socket.close()

def handle_client(client_socket, username):
    """Handle messages from a specific client."""
    while True:
        try:
            message = client_socket.recv(1024).decode()

            if message.startswith("@"):
                # Private message format: @username: message
                target_username, private_message = message[1:].split(":", 1)
                if target_username in clients:
                    clients[target_username].send(f"[Private from {username}]: {private_message}".encode())
                else:
                    client_socket.send(f"User {target_username} not found.".encode())
            else:
                # Broadcast the message to everyone
                broadcast(f"{username}: {message}", client_socket)
        except:
            print(f"{username} disconnected.")
            client_socket.close()
            del clients[username]
            break

def accept_connections():
    """Accept new client connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server running on {HOST}:{PORT}")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")

        # Receive username from the client
        client_socket.send("Enter your username:".encode())
        username = client_socket.recv(1024).decode()
        clients[username] = client_socket

        print(f"{username} joined the chat.")
        broadcast(f"{username} has joined the chat.", client_socket)
        client_socket.send("You are now connected!".encode())

        # Handle the client in a new thread
        threading.Thread(target=handle_client, args=(client_socket, username)).start()

accept_connections()
