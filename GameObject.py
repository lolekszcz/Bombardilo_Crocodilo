#draw innit wys szer x y, kolizje
import pygame

class GameObject:
    def __init__(self, x, y, szer, wys, img_path):
        self.x = x
        self.y = y
        self.szer = szer
        self.wys = wys
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (szer, wys))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.szer, self.wys)

    def collides_with(self, other):
        return self.get_rect().colliderect(other.get_rect())

    def move_if_no_collision(self, dx, dy, other_objects):
        new_rect = self.get_rect().move(dx, dy)
        for obj in other_objects:
            if obj is not self and new_rect.colliderect(obj.get_rect()):
                return  # kolizja – no nie poruszysz się
        # brak kolizji – byczku możesz się poruszać dowolnie

        self.x += dx
        self.y += dy
