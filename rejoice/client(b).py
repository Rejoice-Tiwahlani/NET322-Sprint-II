import socket
from concurrent.futures import ThreadPoolExecutor

def handle_client(client_socket, address):
    print(f"Connection from {address[0]}:{address[1]}")
    
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.send(data)
    
    client_socket.close()
    print(f"Connection closed with {address[0]}:{address[1]}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 45000))
    server_socket.listen(5)
    print("Server started, waiting for connections...")
    
    executor = ThreadPoolExecutor(max_workers=10)
    
    while True:
        client_socket, address = server_socket.accept()
        executor.submit(handle_client, client_socket, address)

if __name__ == "__main__":
    main()


