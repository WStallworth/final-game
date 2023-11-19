from game_constants import *
import pygame
from fireball import Fireball,enemy_fireballs

class Wizard(pygame.sprite.Sprite):
    """My player class"""

    def __init__(self, x, y, image, target):
        super().__init__()
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.target = target
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        if self.rect.x != self.target.rect.x or self.rect.y != self.target.rect.y:
            try:
                self.rect.x += (self.target.rect.x - self.rect.x) / abs(self.target.rect.x - self.rect.x) * WIZARD_SPEED
                self.rect.y += (self.target.rect.y - self.rect.y) / abs(self.target.rect.y - self.rect.y) * WIZARD_SPEED
            except ZeroDivisionError:
                try:
                    self.rect.y += (self.target.rect.y - self.rect.y) / abs(
                        self.target.rect.y - self.rect.y) * WIZARD_SPEED
                except:
                    pass


wizards = pygame.sprite.Group()


