import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projectile Shooter")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Define the Projectile class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, target_x, target_y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
        self.target_x = target_x
        self.target_y = target_y
        self.speed = 10

    def update(self):
        # Calculate the angle between the projectile and the target
        angle = math.atan2(self.target_y - self.rect.centery, self.target_x - self.rect.centerx)

        # Calculate the velocity components
        velocity_x = self.speed * math.cos(angle)
        velocity_y = self.speed * math.sin(angle)

        # Update the projectile's position based on velocity
        self.rect.x += velocity_x
        self.rect.y += velocity_y

# Create sprite groups
all_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Shoot a projectile from the center of the screen to the mouse click
            projectile = Projectile(WIDTH // 2, HEIGHT // 2, *pygame.mouse.get_pos())
            all_sprites.add(projectile)
            projectiles.add(projectile)

    # Update
    all_sprites.update()

    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
