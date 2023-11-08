import socket

# Define the server's host and port
server_host = "127.0.0.1"
server_port = 8080

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_host, server_port))

# Request a file from the server
filename = input("Enter the filename you want to request from the server: ")
client_socket.send(filename.encode())

# Receive the file from the server
data = client_socket.recv(1024)
if data == b"File not found":
    print("File not found on the server.")
else:
    with open(filename, "wb") as file:
        while data:
            file.write(data)
            data = client_socket.recv(1024)
        print(f"File '{filename}' received successfully.")

# Close the client socket
client_socket.close()
