import socket
import time

class Client():
    def __init__(self,host,port):
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientsocket.connect((host,port))
        self.clientsocket.send(bytes('s:hello', 'utf-8'))
        self.host=host
        self.port=port
        self.ready=False
    def run(self):
        self.receive()
        self.send('s:alive')
    def receive(self):
        self.buf = self.clientsocket.recv(1024).decode()
        print(self.buf)
        return self.buf

    def send(self,message):
        self.clientsocket.send(bytes(f'{message}', 'utf-8'))
        time.sleep(0.001)
# client1=Client('127.0.0.1', 12345)
# client1.run()