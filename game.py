import pygame
import time
class Game():
    def __init__(self,width,heigth):
        pygame.init()
        self.width=width
        self.height=heigth
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.running=True
    def run(self):
        while self.running:
            self.screen.fill((255,255,255))
            self.controls()
            pygame.display.update()
            time.sleep(0.01)
        pygame.quit()
    def controls(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running=False