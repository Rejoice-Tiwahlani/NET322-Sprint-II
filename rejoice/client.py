import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, client_socket, address):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.address = address
    
    def run(self):
        print(f"Connection from {self.address[0]}:{self.address[1]}")
        
        while True:
            data = self.client_socket.recv(1024)
            if not data:
                break
            self.client_socket.send(data)
        
        self.client_socket.close()
        print(f"Connection closed with {self.address[0]}:{self.address[1]}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8080))
    server_socket.listen(5)
    print("Server started, waiting for connections...")
    
    while True:
        client_socket, address = server_socket.accept()
        client_thread = ClientThread(client_socket, address)
        client_thread.start()

if __name__ == "__main__":
    main()
