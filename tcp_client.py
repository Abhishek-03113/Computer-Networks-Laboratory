import socket

# Server configuration
server_ip = "127.0.0.1"
server_port = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))

# Send a message to the server_ip
message = input("Enter Message to send To Server : ")
client_socket.send(message.encode())
print("Thank You for your message, waiting for servers response ....")

# Receive the server's response
response = client_socket.recv(1024).decode()
print(f"Received from server: {response}")

print("Closing Connection")
# Close the client socket
client_socket.close()
