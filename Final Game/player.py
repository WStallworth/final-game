import pygame
from game_constants import *

class Player(pygame.sprite.Sprite):
    """My player class"""

    def __init__(self,x,y,element,element_pic_path):
        super().__init__()
        self.image = pygame.image.load(element_pic_path)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        self.x_speed = 0
        self.y_speed = 0


    def draw(self,surface):
        surface.blit(self.image,(self.rect.center))

    def move_up(self):
        self.y_speed = -1 * PLAYER_SPEED

    def move_down(self):
        self.y_speed = PLAYER_SPEED

    def move_left(self):
        self.x_speed = -1 * PLAYER_SPEED
        #self.image = self.reverse_image

    def move_right(self):
        self.x_speed = PLAYER_SPEED
        #self.image = self.forward_image

    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed