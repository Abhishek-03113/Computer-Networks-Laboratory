import socket
import os

# Define the server's host and port
server_host = "127.0.0.1"
server_port = 8080


# Function to send a file to the client
def send_file(client_socket, filename):
    try:
        with open(filename, "rb") as file:
            data = file.read(1024)
            while data:
                client_socket.send(data)
                data = file.read(1024)
            print(f"File '{filename}' sent successfully.")
    except FileNotFoundError:
        client_socket.send("File not found".encode())
        print(f"File '{filename}' not found.")


# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((server_host, server_port))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server is listening on {server_host}:{server_port}")

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Receive the filename request from the client
    filename = client_socket.recv(1024).decode()

    # Send the requested file to the client
    send_file(client_socket, filename)

    # Close the client socket
    client_socket.close()

# Close the server socket
server_socket.close()

"""
Server is listening on 127.0.0.1:8080
Accepted connection from ('127.0.0.1', 55196)
File 'ass4.py' sent successfully.



"""
