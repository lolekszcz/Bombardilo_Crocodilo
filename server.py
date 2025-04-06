import socket
class Server:
    def __init__(self,HOST):
        self.HOST=HOST
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind(('localhost', 8089))
        self.serversocket.listen(5)  # become a server socket, maximum 5 connections
        self.clients = set()

    def run(self):
        buf=''
        while True:
            print('aaa')
            print(buf)
            connection, address = self.serversocket.accept()
            print(connection, address)
            print('bbb')
            if connection not in self.clients:
                self.clients.add(connection)
                for c in self.clients:
                    c.sendall(bytes(f"hello back. number of players: {len(self.clients)}", 'utf-8'))
            print('ccc')
            buf = connection.recv(1024).decode()
            print('ddd')
            if len(buf) > 0:
                print(buf,"\n")


server1=Server(8089)
server1.run()











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





