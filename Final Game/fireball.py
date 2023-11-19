from game_constants import *
import pygame
import math

class Fireball(pygame.sprite.Sprite):
    def __init__(self, image, start_x, start_y, target_x, target_y):
        super().__init__()
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (start_x,start_y)
        self.target_x = target_x
        self.target_y = target_y
        self.speed = PROJECTILE_SPEED
        self.start_x = start_x
        self.start_y = start_y

    #THIS CODE IS FROM CHAT GPT I CHANGED SOME OF THE CLASS PARAMETERS
    def update(self):
        # Calculate the angle between the projectile and the target
        angle = math.atan2(self.target_y - self.start_y, self.target_x - self.start_x)
        # Calculate the velocity components
        velocity_x = self.speed * math.cos(angle)
        velocity_y = self.speed * math.sin(angle)

        # Update the projectile's position based on velocity
        self.rect.x += velocity_x
        self.rect.y += velocity_y

        if self.rect.x > SCREEN_WIDTH or self.rect.x < 0 or self.rect.y > SCREEN_HEIGHT or self.rect.y < 0:
            self.kill()
    #TODO: FIGURE THIS OUT
    def enemy(self):
        # Calculate the angle between the projectile and the target
        angle = math.atan2(self.target_y - self.rect.centery, self.target_x - self.rect.centerx)

        # Calculate the velocity components
        velocity_x = self.speed * math.cos(angle)
        velocity_y = self.speed * math.sin(angle)

        # Update the projectile's position based on velocity
        self.rect.x += velocity_x
        self.rect.y += velocity_y

    def draw(self,surface):
        surface.blit(self.image,self.rect.center)


fireballs = pygame.sprite.Group()
enemy_fireballs = pygame.sprite.Group()