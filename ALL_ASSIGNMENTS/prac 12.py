import socket

def ip_to_url(ip_address):
    try:
        url = socket.gethostbyaddr(ip_address)
        return f"IP: {ip_address} maps to URL: {url[0]}"
    except socket.herror:
        return "Hostname not found for the provided IP address."

def url_to_ip(url):
    try:
        ip = socket.gethostbyname(url)
        return f"URL: {url} resolves to IP: {ip}"
    except socket.gaierror:
        return "IP address not found for the provided URL."

while True:
    choice = input("Choose operation (1 for IP to URL, 2 for URL to IP, 0 to exit): ")
    
    if choice == '1':
        ip_address = input("Enter the IP address: ")
        result = ip_to_url(ip_address)
        print(result)
    elif choice == '2':
        url = input("Enter the URL: ")
        result = url_to_ip(url)
        print(result)
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 0 to exit.")