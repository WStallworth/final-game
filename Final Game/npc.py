import pygame
from game_constants import *
import random
import sys
class NPC(pygame.sprite.Sprite):
    """My player class"""

    def __init__(self,x,y,image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        self.x_speed = 0
        self.y_speed = 0


    def draw(self,surface):
        surface.blit(self.image,self.rect)

    def update(self):
        clock = pygame.time.Clock()
        # Move randomly
        direction = random.choice(["up", "down", "left", "right"])
        if direction == "up":
            self.y_speed = -1 * NPC_SPEED
        elif direction == "down":
            self.y_speed = NPC_SPEED
        elif direction == "left":
            self.x_speed = -1 * NPC_SPEED
        elif direction == "right":
            self.x_speed = NPC_SPEED
        clock.tick()
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x > SCREEN_WIDTH - 2 * BASETILE_SIZE:
            self.x = SCREEN_WIDTH - 2 * BASETILE_SIZE
        if self.x < BASETILE_SIZE:
            self.x = BASETILE_SIZE
        if self.y < BASETILE_SIZE:
            self.y = BASETILE_SIZE
        if self.y > SCREEN_HEIGHT - (BASETILE_SIZE * 2):
            self.y = SCREEN_HEIGHT - (BASETILE_SIZE * 2)
        self.rect.x = self.x
        self.rect.y = self.y



NPCS = pygame.sprite.Group()
