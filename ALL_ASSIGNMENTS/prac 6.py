#server
import socket
def main():
    host = "127.0.0.1"
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print("Waiting for a connection...")
    conn, addr = s.accept()
    print(f"Connection from: {str(addr)}")
    with open('received_file.txt', 'wb') as file:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)
    print("File received successfully.")
    conn.close()
if __name__ == '__main__':
    main()


#client
import socket
def main():
    host = "127.0.0.1"
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    file_name = input("Enter the name of the file to send: ")
    with open(file_name, 'rb') as file:
        data = file.read(1024)
        while data:
            s.send(data)
            data = file.read(1024)
    print("File sent successfully.")
    s.close()
if __name__ == '__main__':
    main()
