import pygame

class GUI:
    def __init__(self):
        self.ribbon1 = pygame.image.load("ribbonR.png")
        self.ribbon2 = pygame.image.load("bribbonR.png")
        self.ribbon3 = pygame.image.load("RribbonR.png")

    def draw(self, screen):
        screen.blit(self.ribbon1, (10, 20))
        screen.blit(self.ribbon2, (400, 20))
        screen.blit(self.ribbon3, (800, 20))
