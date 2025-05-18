import socket
import threading

# Client Configuration
HOST = '172.20.10.6'  # Server IP
PORT = 12345

def receive_messages(client_socket):
    """Receive messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print("Disconnected from the server.")
            client_socket.close()
            break

def send_messages(client_socket):
    """Send messages to the server."""
    while True:
        message = input()
        client_socket.send(message.encode())

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Receive the prompt for username
print(client_socket.recv(1024).decode())
username = input()
client_socket.send(username.encode())

# Start threads for sending and receiving messages
threading.Thread(target=receive_messages, args=(client_socket,)).start()
threading.Thread(target=send_messages, args=(client_socket,)).start()
