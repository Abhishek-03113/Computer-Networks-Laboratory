#server
import socket
def main():
    host = "127.0.0.1"
    port = 12346
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    print("UDP server is listening on port", port)
    while True:
        data, addr = s.recvfrom(1024)
        if not data:
            break
        if data.startswith(b"FILE_NAME:"):
            filename = data.decode()[10:]
            with open(filename, 'wb') as file:
                while True:
                    data, addr = s.recvfrom(1024)
                    if not data:
                        break
                    file.write(data)
                print(f"File '{filename}' received successfully.")

if __name__ == '__main__':
    main()


#client
import socket
def send_file(filename, host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(b"FILE_NAME:" + filename.encode(), (host, port))
    
    with open(filename, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            s.sendto(data, (host, port))
        file.close()
        s.sendto(b"", (host, port))
        print(f"File '{filename}' sent successfully.")
    s.close()

if __name__ == '__main__':
    host = "127.0.0.1"
    port = 12346
    filename = input("Enter the filename to send: ")
    send_file(filename, host, port)
