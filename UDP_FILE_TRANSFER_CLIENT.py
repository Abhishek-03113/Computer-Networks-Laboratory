import socket

# Define the server's host and port
server_host = "127.0.0.1"
server_port = 8080

# Create a UDP socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Request a file from the server
filename = input("Enter the filename you want to request from the server: ")
client_socket.sendto(filename.encode(), (server_host, server_port))

while True:
    # Receive the file from the server
    data, server_address = client_socket.recvfrom(1024)
    if data == b"File not found":
        print("File not found on the server.")
        break
    with open(filename, "ab") as file:
        file.write(data)
    print(f"Received data from {server_address}.")

print(f"File '{filename}' received successfully.")

# Close the client socket
client_socket.close()

"""
Enter the filename you want to request from the server: 5_2.cpp
Received data from ('127.0.0.1', 8080).

"""
