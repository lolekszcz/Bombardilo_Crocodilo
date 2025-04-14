import pygame
import random
import math



class MapGenerator:
    def __init__(self, rows, cols, tile_size=10):
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.map = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        square_point1 = (random.randint(50,100), random.randint(50,100))
        square_point2 = (random.randint(cols - 100,cols - 50), random.randint(rows - 100,rows - 50))

        points = [(random.randint(square_point1[0],square_point2[0]),
                   random.randint(square_point1[1],square_point2[1]))for i in range(10)] # points (x,y)

        for point in points:
            for y in range(rows):
                for x in range(cols):
                    dist = math.sqrt((point[0] - x)**2 + (point[1] - y)**2)
                    if dist < 50:
                        self.map[y][x] = 1
                    elif 60 > dist > 50:
                        self.map[y][x] = 2


        self.tiles = {
            0: pygame.image.load('Tiny Swords/Ground/000.png'),
            1: pygame.image.load('Tiny Swords/Ground/104.png'),
            2: pygame.image.load('Tiny Swords/Ground/204.png')
        }

        for key in self.tiles:
            self.tiles[key] = pygame.transform.scale(self.tiles[key], (self.tile_size, self.tile_size))

    def draw(self, screen):
        for y in range(self.rows):
            for x in range(self.cols):
                tile_value = self.map[y][x]
                image = self.tiles[tile_value]
                screen.blit(image, (x * self.tile_size, y * self.tile_size))




pygame.init()
screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Map Generator")

map_generator = MapGenerator(500, 500, tile_size=2)

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    map_generator.draw(screen)

    pygame.display.flip()

pygame.quit()