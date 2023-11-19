import pygame
from game_constants import *

class Player(pygame.sprite.Sprite):
    """My player class"""

    def __init__(self,x,y,weapon,element_pic_path):
        super().__init__()
        self.image = pygame.image.load(element_pic_path)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        self.speed = PLAYER_SPEED
        self.weapon = weapon


    def draw(self,surface):
        surface.blit(self.image,self.rect)

    #CASEY CODE
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > BASETILE_SIZE*1.25:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < SCREEN_WIDTH-BASETILE_SIZE*1.25:
            self.rect.x += self.speed
        if keys[pygame.K_w] and self.rect.top > BASETILE_SIZE*1.25:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT-BASETILE_SIZE*1.25:
            self.rect.y += self.speed

