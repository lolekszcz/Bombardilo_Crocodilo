import socket
import time
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
clientsocket.send(bytes('hello','utf-8'))
clientsocket.send(bytes('hello2','utf-8'))
clientsocket.send(bytes('hello3','utf-8'))
clientsocket.send(bytes('hello4','utf-8'))
while True:
    buf=clientsocket.recv(1024).decode()
    if len(buf) > 0:
        print (buf)
    time.sleep(5)
    clientsocket.send(bytes(f'understood:{buf}', 'utf-8'))
    print('sent')

# import socket
# class Client:
#     def __init__(self,HOST):
#         self.HOST=HOST
#         self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.clientsocket.connect(('localhost', HOST))
#         self.id=-1
#     def add_self(self):
#         self.clientsocket.send(bytes(f'hello from new player','utf-8'))
#     def get_id(self):
#         if self.id==-1:
#             if type(self.buf)==str:
#                 try:
#                     if self.buf[0:9]=='player_id':
#                         self.id=int(self.buf[10:len(self.buf)])
#                 except:
#                     pass
#             print(self.id)
#
#
#     def run(self):
#         while True:
#             self.buf = self.clientsocket.recv(1024)
#             if self.buf != None:
#                 self.buf=self.buf.decode()
#                 print(self.buf, 'aaaa')
#                 self.get_id()
# client1=Client(8089)
# client1.run()