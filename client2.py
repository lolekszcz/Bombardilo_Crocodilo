import socket
class Client:
    def __init__(self,HOST):
        self.HOST=HOST
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientsocket.connect(('localhost', HOST))
        self.id=-1
        self.add_self()
    def add_self(self):
        self.clientsocket.send(bytes(f'hello from new player1'))
    def get_id(self):
        if self.id==-1:
            if type(self.buf)==str:
                try:
                    if self.buf[0:9]=='player_id':
                        self.id=int(self.buf[10:len(self.buf)])
                except:
                    pass
            print(self.id)


    def run(self):
        while True:
            self.buf = self.clientsocket.recv(1024)
            if self.buf != None:
                self.buf=self.buf.decode()
                print(self.buf, 'aaaa')
                self.get_id()
client2=Client(8089)
client2.run()