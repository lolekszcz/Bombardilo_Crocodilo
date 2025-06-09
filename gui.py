import pygame

class GUI:
    def __init__(self):
        self.ribbon1 = pygame.image.load("ribbonR.png")
        self.ribbon2 = pygame.image.load("bribbonR.png")
        self.ribbon3 = pygame.image.load("RribbonR.png")
        self.icon1 = pygame.image.load("money.png")
        self.icon2 = pygame.image.load("wood.png")
        self.icon3 = pygame.image.load("meat.png")
        self.banner1 = pygame.image.load("banner_down.png")

    def draw(self, screen):
        screen.blit(self.ribbon1, (10, 20))
        screen.blit(self.ribbon2, (300, 20))
        screen.blit(self.ribbon3, (500, 20))
        screen.blit(self.icon1, (20, 20))
        screen.blit(self.icon2, (310, 20))
        screen.blit(self.icon3, (510, 20))
        screen.blit(self.banner1, (20, 610))
