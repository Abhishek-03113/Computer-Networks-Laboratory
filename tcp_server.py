import socket

# Server configuration
server_ip = "127.0.0.1"
server_port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server is listening on {server_ip}:{server_port}")

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Receive data from the client
    data = client_socket.recv(1024).decode()
    print(f"Received from client: {data}")

    print("Sending response to client ... ")

    # Send a response to the client
    response = "its 200, everythings fine on server side"

    client_socket.send(response.encode())

    # Close the client socket
    client_socket.close()
