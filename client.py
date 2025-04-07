import socket
import time

class Client():
    def __init__(self,host,port):
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientsocket.connect((host,port))
        self.clientsocket.send(bytes('hello', 'utf-8'))
        self.host=host
        self.port=port
        self.ready=False
    def run(self):
        print('bbb')
        self.receive()
        self.send('aaa')
    def receive(self):
        buf = self.clientsocket.recv(1024).decode()
        time.sleep(0.01)
        return buf

    def send(self,message):
        self.clientsocket.send(bytes(f'{message}', 'utf-8'))
# client1=Client('127.0.0.1', 12345)
# client1.run()