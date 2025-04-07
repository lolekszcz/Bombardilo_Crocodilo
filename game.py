import pygame
import time
import tkinter as tk

class Game():
    def __init__(self,width,heigth):
        pygame.init()
        self.width=width
        self.height=heigth
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.running=True
        self.font = pygame.font.SysFont('Arial', 36)
        self.button = Button('Start_button.png', self.width // 2 - 150, self.height - 200, 500, 75, 'START', self.font, (255, 255, 255))
    def run(self):
        while self.running:
            self.screen.fill((255,255,255))
            self.controls()
            self.button.draw(self.screen)
            pygame.display.update()
            time.sleep(0.01)
        pygame.quit()
    def controls(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running=False
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     mouse_pos = pygame.mouse.get_pos()
            #     if self.button.is_clicked(mouse_pos):
            #         print("Button clicked!")

class Button:
    def __init__(self, image, x, y, width, height, text=None, font=None, text_color=(0, 0, 0)):
        self.image = pygame.image.load('Start_button.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.text = text
        self.font = font
        self.text_color = text_color

        if self.text and self.font:
            self.text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = self.text_surface.get_rect(center=self.rect.center)
            self.image.blit(self.text_surface, (100, 100))

    def draw(self, screen):
        screen.blit(self.image, self.rect)