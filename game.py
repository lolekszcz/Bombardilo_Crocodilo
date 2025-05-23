import pygame
import time
import map
from pygame import MOUSEBUTTONDOWN
from gui import *
import random
import client

class Game():
    def __init__(self,width,heigth):
        pygame.init()
        self.join()
        self.state = 'start'
        # self.gui = GUI()
        self.ox=0
        self.oy=0
        self.map_speed=10
        self.width=width
        self.height=heigth
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.running=True
        self.game_start=False
        self.ready=False
        self.wheel_speed=1.5
        self.button = Button('Start_button.png',400,800,100,100)
        clicked = False
        counter = 0
        self.w=False
        self.s=False
        self.ac=False
        self.dc=False
    def run(self):
        while self.running:
            self.screen.fill((255,255,255))
            if self.game_start==True:
                if type(self.Map_Generator)==map.MapGenerator:
                    print('aaa')
                    self.Map_Generator.draw(self.screen,self.d,self.ox,self.oy)

            if self.s:
                self.oy -= self.map_speed
            if self.w:
                self.oy += self.map_speed
            if self.dc:
                self.ox -= self.map_speed
            if self.ac:
                self.ox += self.map_speed

            if self.client!=None:
                self.client.run()
                self.handle_message(self.client.buf)
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        self.ready_up()
                        print('rr')
                    if event.key==pygame.K_w:
                        self.w=True
                    if event.key==pygame.K_s:
                        self.s=True
                    if event.key==pygame.K_a:
                        self.ac=True
                    if event.key==pygame.K_d:
                        self.dc=True
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_w:
                        self.w=False
                    if event.key==pygame.K_s:
                        self.s=False
                    if event.key==pygame.K_a:
                        self.ac=False
                    if event.key==pygame.K_d:
                        self.dc=False
                if event.type==pygame.MOUSEWHEEL:
                    if event.y==1:
                        self.d*=self.wheel_speed
                        print('cccc')
                    if event.y==-1:
                        self.d*=1/self.wheel_speed



                if self.button.collide(pos) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                    self.state = 'game'


            if self.state == 'start':
                self.button.draw(self.screen)

            if self.state == 'game':
                self.gui.draw(self.screen)

            pygame.display.update()
        if self.ready:
            self.ready_up()
        self.client.send('s:player_disconnected')

        pygame.quit()


    def handle_message(self,data):
        for d in data:
            d=d.split(":")
            if d[0] == "s":
                if d[1]=="game_started":
                    self.game_start=True
                    self.start_the_game()
            elif d[0]=="seed":
                self.seed=d[1]
                print(self.seed)

    def start_the_game(self):
        self.d=8
        self.Map_Generator=map.MapGenerator(self.width//self.d,self.height//self.d,self.seed,self.d,tile_size=2)

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