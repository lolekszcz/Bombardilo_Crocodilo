import pygame
import time

from pygame import MOUSEBUTTONDOWN
from gui import *

import client

class Game():
    def __init__(self,width,heigth):
        pygame.init()
        self.join()
        self.state = 'start'
        # self.gui = GUI()
        self.width=width
        self.height=heigth
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.running=True
        self.game_start=False
        self.ready=False

        self.button = Button('Start_button.png',400,800,100,100)
        clicked = False
        counter = 0
    def run(self):
        while self.running:
            self.screen.fill((255,255,255))
            self.controls()


            if self.client!=None:
                self.client.run()

            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        self.ready_up()
                        print('rr')
                if self.button.collide(pos) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                    self.state = 'game'


            if self.state == 'start':
                self.button.draw(self.screen)

            if self.state == 'game':
                self.gui.draw(self.screen)

            pygame.display.update()
            time.sleep(0.01)
        if self.ready:
            self.ready_up()
        self.client.send('s:player_disconnected')

        pygame.quit()

    def controls(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running=False

    def ready_up(self):
        if self.ready==False:
            self.ready=True
            self.client.send('s:player_ready')


        else:
            self.ready=False
            self.client.send('s:player_not_ready')

    def join(self):
        self.client = client.Client("127.0.0.1", 12345)
        print('aaa')

class Button:
    def __init__(self, image, x, y, width, height, text=None, font=None, text_color=(0, 0, 0)):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.text = text
        self.font = font
        self.text_color = text_color

        if self.text and self.font:
            self.text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = self.text_surface.get_rect(center=self.rect.center)
            self.image.blit(self.text_surface, (100, 100))

    def collide(self, pos):
        if self.rect.collidepoint(pos):
            return True
        return False


    def draw(self, screen):
        pos = pygame.mouse.get_pos()
        screen.blit(self.image, self.rect)