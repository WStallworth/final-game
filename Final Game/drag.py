import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Continuous Create Sprites while Button Pressed")

# Define colors
white = (255, 255, 255)

# Define a simple sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Create a sprite group
sprites = pygame.sprite.Group()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Create a new sprite on mouse down
            #new_sprite = Sprite(*event.pos)
            #sprites.add(new_sprite)
        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            # Create a new sprite while the left mouse button is pressed and mouse is moving
            new_sprite = Sprite(*event.pos)
            sprites.add(new_sprite)

    screen.fill((0, 0, 0))

    # Draw sprites
    sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
