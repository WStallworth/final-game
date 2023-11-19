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

    def update(self):
        # Calculate the angle between the projectile and the target
        angle = math.atan2(self.target_y - self.rect.centery, self.target_x - self.rect.centerx)

        # Calculate the velocity components
        velocity_x = self.speed * math.cos(angle)
        velocity_y = self.speed * math.sin(angle)

        # Update the projectile's position based on velocity
        self.rect.x += velocity_x
        self.rect.y += velocity_y

        if math.dist((self.rect.x, self.rect.y), (self.target_x, self.target_y)) <= (self.speed+6):
            self.kill()

    def draw(self,surface):
        surface.blit(self.image,self.rect.center)


fireballs = pygame.sprite.Group()