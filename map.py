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
                        self.map[y][x] = 104
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
                            elif tile == 104:
                                grass_nearby = True
                        if water_nearby and grass_nearby:
                            break
                    if water_nearby and grass_nearby:
                        break


                # insert appropriate sand tile texture depending on neighbouring water
                if water_nearby and grass_nearby:
                    # Determine direction of surrounding tiles for edge placement
                    up = self.map[y - 1][x]
                    down = self.map[y + 1][x]
                    left = self.map[y][x - 1]
                    right = self.map[y][x + 1]

                    if up == 0:
                        new_map[y][x] = 201  # grass above, water below
                    elif down == 104 and up == 0:
                        new_map[y][x] = 205  # grass below, water above
                    elif left == 104 and right == 0:
                        new_map[y][x] = 201  # grass left, water right
                    elif right == 104 and left == 0:
                        new_map[y][x] = 207  # grass right, water left
                    else:
                        new_map[y][x] = 204  # default sand

        self.map = new_map
        print(self.map)

        self.tiles = {
            0: pygame.image.load('Tiny Swords/Ground/000.png'),
            100: pygame.image.load('Tiny Swords/Ground/100.png'),
            101: pygame.image.load('Tiny Swords/Ground/101.png'),
            102: pygame.image.load('Tiny Swords/Ground/102.png'),
            103: pygame.image.load('Tiny Swords/Ground/103.png'),
            104: pygame.image.load('Tiny Swords/Ground/104.png'),
            105: pygame.image.load('Tiny Swords/Ground/105.png'),
            106: pygame.image.load('Tiny Swords/Ground/106.png'),
            107: pygame.image.load('Tiny Swords/Ground/107.png'),
            108: pygame.image.load('Tiny Swords/Ground/108.png'),
            110: pygame.image.load('Tiny Swords/Ground/110.png'),
            111: pygame.image.load('Tiny Swords/Ground/111.png'),
            112: pygame.image.load('Tiny Swords/Ground/112.png'),
            120: pygame.image.load('Tiny Swords/Ground/120.png'),
            121: pygame.image.load('Tiny Swords/Ground/121.png'),
            122: pygame.image.load('Tiny Swords/Ground/122.png'),
            130: pygame.image.load('Tiny Swords/Ground/130.png'),
            200: pygame.image.load('Tiny Swords/Ground/200.png'),
            201: pygame.image.load('Tiny Swords/Ground/201.png'),
            202: pygame.image.load('Tiny Swords/Ground/202.png'),
            203: pygame.image.load('Tiny Swords/Ground/203.png'),
            204: pygame.image.load('Tiny Swords/Ground/204.png'),
            205: pygame.image.load('Tiny Swords/Ground/205.png'),
            206: pygame.image.load('Tiny Swords/Ground/206.png'),
            207: pygame.image.load('Tiny Swords/Ground/207.png'),
            208: pygame.image.load('Tiny Swords/Ground/208.png'),
            210: pygame.image.load('Tiny Swords/Ground/210.png'),
            211: pygame.image.load('Tiny Swords/Ground/211.png'),
            212: pygame.image.load('Tiny Swords/Ground/212.png'),
            220: pygame.image.load('Tiny Swords/Ground/220.png'),
            221: pygame.image.load('Tiny Swords/Ground/221.png'),
            222: pygame.image.load('Tiny Swords/Ground/222.png'),
            230: pygame.image.load('Tiny Swords/Ground/230.png')
        }

        for key in self.tiles:
            self.tiles[key] = pygame.transform.scale(self.tiles[key], (self.tile_size, self.tile_size))

    def draw(self, screen):
        for y in range(self.rows):
            for x in range(self.cols):
                tile_value = self.map[y][x]
                image = self.tiles[tile_value]
                screen.blit(image, (x * self.tile_size, y * self.tile_size))




# pygame.init()
# screen_width, screen_height = 1000, 1000
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Map Generator")
#
# map_generator = MapGenerator(500, 500, tile_size=2)
#
#
# running = True
# while running:
#     screen.fill((255, 255, 255))
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
#             map_generator = MapGenerator(500, 500, tile_size=2)
#
#     map_generator.draw(screen)
#
#
#
#     pygame.display.flip()
#
# pygame.quit()