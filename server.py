import socket
import threading

def get_local_ip():
    # Connect to an external server to find the local IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)

    try:
        # Try to connect to a public server (Google's DNS server)
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]  # This will get the local IP address
    except Exception:
        local_ip = '127.0.0.1'  # If there's an error (e.g., no network), return localhost
    finally:
        s.close()

    return local_ip
class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.s = socket.socket()

        self.ip = get_local_ip()
        self.ip = '127.0.0.1'

        print("Server is running on " + self.ip)

        self.s.bind((self.ip, port))
        self.s.listen(5)

        self.clients = []
        self.players = []
        self.walls = []


        print("socket is listening")
        return

    def handle_client(self, client_socket, client_id):
        # This function will handle data exchange with a single client
        while True:
            try:
                # Receive data from the client
                data_raw = client_socket.recv(1024)  # 1024 is the buffer size
                if not data_raw:
                    # If no data is received, the client has disconnected
                    break

                data_temp = data_raw.decode()
                print(data_temp)


                            # print(f"Player num: {len(self.players)}")
                            # print(f"Client position: {posX},{posY}

                # Process the data and send a response back to the client


                client_socket.send('xxx'.encode())
            except Exception as e:
                print(f"Error: {e}")
                break

        # Close the connection if the client disconnects
        print("Closing connection...")
        self.players.pop(client_id)
        client_socket.close()
    def update_server(self):
        # Establish connection with client.
        c, addr = self.s.accept()

        if c not in self.clients:
            print('Got connection from', addr)

            # send a thank you message to the client. encoding to send byte type.
            c.send('Thank you for connecting'.encode())

            self.clients.append(c)
            # Create a new thread to handle this client separately
            client_thread = threading.Thread(target=self.handle_client, args=(c,len(self.clients)-1))
            client_thread.start()


# Start the servers
def start_server(port):
    server = Server("127.0.0.1", 12345)
    return server

server = start_server(34)

while True:
    server.update_server()











# import socket
# # become a server socket, maximum 5 connections
# class Server():
#     def __init__(self,HOST):
#         self.clients = set()
#         self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.serversocket.bind(('localhost', HOST))
#         self.serversocket.listen(5)
#     def new_connection(self):
#         connection, address = self.serversocket.accept()
#         self.clients.add(connection)
#     def run(self):
#         while True:
#             connection, address = self.serversocket.accept()
#             # self.clients.add(connection)
#             # print(self.clients)
#             data = connection.recv(1024).decode()
#             print(data)
#             # if connection in self.clients:
#             #     pass
#             # else:
#             #
#             #     connection.sendall(bytes(f"player_id {len(self.clients)}", 'utf-8'))
#
#             # for client in self.clients:
#             #     client.sendall(bytes(f"{data} from host", 'utf-8'))
# server1=Server(8089)
# server1.run()





