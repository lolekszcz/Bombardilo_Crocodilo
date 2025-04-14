import pygame
import random
import math



class MapGenerator:
    def __init__(self, rows, cols, tile_size=10):
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.map = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        core_points = [
            (100, 100),  # top-left
            (self.cols - 100, 100),  # top-right
            (100, self.rows - 100),  # bottom-left
            (self.cols - 100, self.rows - 100)  # bottom-right
        ]

        # 2. Generate additional points between the corners to connect the island
        min_x = min(p[0] for p in core_points)
        max_x = max(p[0] for p in core_points)
        min_y = min(p[1] for p in core_points)
        max_y = max(p[1] for p in core_points)

        additional_points = [
            (random.randint(min_x, max_x), random.randint(min_y, max_y))
            for _ in range(16)
        ]

        # Combine all points
        points = core_points + additional_points

        for point in points:
            for y in range(rows):
                for x in range(cols):
                    dist = math.sqrt((point[0] - x)**2 + (point[1] - y)**2)
                    if dist < 80:
                        self.map[y][x] = 1
                    pass

        # Second pass: create thicker sand borders (10 tiles wide)
        border_thickness = 5
        new_map = [row[:] for row in self.map]  # Make a copy so we don’t overwrite while checking

        for y in range(border_thickness, self.rows - border_thickness):
            for x in range(border_thickness, self.cols - border_thickness):
                current = self.map[y][x]
                water_nearby = False
                grass_nearby = False

                for dy in range(-border_thickness, border_thickness + 1):
                    for dx in range(-border_thickness, border_thickness + 1):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < self.rows and 0 <= nx < self.cols:
                            tile = self.map[ny][nx]
                            if tile == 0:
                                water_nearby = True
                            elif tile == 1:
                                grass_nearby = True
                        if water_nearby and grass_nearby:
                            break
                    if water_nearby and grass_nearby:
                        break

                if water_nearby and grass_nearby:
                    new_map[y][x] = 2

        self.map = new_map


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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            map_generator = MapGenerator(500, 500, tile_size=2)

    map_generator.draw(screen)



    pygame.display.flip()

pygame.quit()