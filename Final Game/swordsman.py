from game_constants import *
import pygame
class Swordsman(pygame.sprite.Sprite):
    """My player class"""

    def __init__(self,x,y,image,target):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.target = target
        self.rect.center = (x,y)
        self.x_speed = 0
        self.y_speed = 0


    def draw(self,surface):
        surface.blit(self.image,self.rect)

    def update(self):
        self.rect.x += (self.target.rect.x - self.rect.x) * ENEMY_SPEED
        self.rect.y += (self.target.rect.y - self.rect.y) * ENEMY_SPEED


swordsmen = pygame.sprite.Group()


