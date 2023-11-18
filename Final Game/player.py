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
        self.x_speed = 0
        self.y_speed = 0
        self.weapon = weapon


    def draw(self,surface):
        surface.blit(self.image,self.rect)

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


    def stop_x(self):
        self.x_speed = 0

    def stop_y(self):
        self.y_speed = 0


    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x > SCREEN_WIDTH - 2*BASETILE_SIZE:
            self.x = SCREEN_WIDTH - 2*BASETILE_SIZE
        if self.x < BASETILE_SIZE:
            self.x = BASETILE_SIZE
        if self.y < BASETILE_SIZE:
            self.y = BASETILE_SIZE
        if self.y > SCREEN_HEIGHT - (BASETILE_SIZE * 2):
            self.y = SCREEN_HEIGHT - (BASETILE_SIZE * 2)
        self.rect.x = self.x
        self.rect.y = self.y