import socket

def echo_server():
    """ A simple echo server """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9090)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print("Server started, waiting for connections...")

    while True:
        print("Waiting for a client...")
        client_socket, client_address = server_socket.accept()
        print("Accepted connection from %s:%s" % client_address)

        try:
            while True:
                data = client_socket.recv(1024)
                if data:
                    print("Received: %s" % data.decode('utf-8'))
                    client_socket.sendall(data)
                else:
                    break
        except socket.error as e:
            print("Socket error: %s" % str(e))
        except Exception as e:
            print("Other exception: %s" % str(e))
        finally:
            print("Closing connection with %s:%s" % client_address)
            client_socket.close()

if __name__ == '__main__':
    echo_server()
