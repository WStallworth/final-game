import pygame
from game_constants import *
class HouseTiles(pygame.sprite.Sprite):
    def __init__(self,image,x=0,y=0):
        super().__init__()
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y =y

    def draw(self,surface):
        surface.blit(self.image, self.rect)

red_house = pygame.sprite.Group()
gray_house = pygame.sprite.Group()
decor = pygame.sprite.Group()