import socket

# Define the server's host and port
server_host = "127.0.0.1"
server_port = 8080


# Function to send a file to the client using UDP
def send_file(client_socket, filename, client_address):
    try:
        with open(filename, "rb") as file:
            data = file.read(1024)
            while data:
                client_socket.sendto(data, client_address)
                data = file.read(1024)
            print(f"File '{filename}' sent successfully to {client_address}.")
    except FileNotFoundError:
        client_socket.sendto("File not found".encode(), client_address)
        print(f"File '{filename}' not found. Sent error message to {client_address}.")


# Create a UDP socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the host and port
server_socket.bind((server_host, server_port))

print(f"Server is listening on {server_host}:{server_port}")

while True:
    # Receive the filename request from the client
    data, client_address = server_socket.recvfrom(1024)
    filename = data.decode()

    # Send the requested file to the client
    send_file(server_socket, filename, client_address)

# Close the server socket (This part won't be reached in the current example)
server_socket.close()
"""
Server is listening on 127.0.0.1:8080
File '5_2.cpp' sent successfully to ('127.0.0.1', 62355).

"""
