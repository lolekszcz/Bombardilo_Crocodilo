import socket
import threading
import time

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

        #getting ready:
        self.ready_players=0
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
                data=data_temp.split(":")
                self.handle_message(data,client_socket)
                print('sent')
            except Exception as e:
                print(f"Error: {e}")
                break

        # Close the connection if the client disconnects
        print("Closing connection...")
        self.players.pop(client_id)
        client_socket.close()
    def handle_message(self,data,client_socket):
        if data[0]=="s":
            if data[1]=="player_ready":
                self.ready_players+=1
            if data[1]=="player_not_ready":
                self.ready_players-=1
            if data[1]=="hello":
                client_socket.send("s:hello_back".encode())
        if self.ready_players>=len(self.clients) and self.ready_players>=1:
                client_socket.send("s:game_started".encode())
                time.sleep(0.001)
        client_socket.send(f"s:number_of_ready_players:{self.ready_players}".encode())
        time.sleep(0.001)
        client_socket.send(f"number_of_players:{len(self.clients)}".encode())
        time.sleep(0.001)


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
















