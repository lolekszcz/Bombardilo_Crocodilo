import pygame
import time
import client
class Game():
    def __init__(self,width,heigth):
        pygame.init()
        self.width=width
        self.height=heigth
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.running=True
        self.join()
    def run(self):
        while self.running:
            self.screen.fill((255,255,255))
            self.controls()
            if self.client!=None:
                self.client.run()
            pygame.display.update()
            time.sleep(0.01)
        pygame.quit()
    def controls(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running=False
    def join(self):
        self.client=client.Client("127.0.0.1", 12345)