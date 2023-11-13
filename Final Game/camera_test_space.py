import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Scrolling Platformer")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up player
player_size = 50
player_color = (0, 128, 255)
player_x, player_y = width // 2 - player_size // 2, height // 2 - player_size // 2
player_speed = 5
jump_height = 10
jumping = False

# Set up platform
platform_width, platform_height = 200, 20
platform_color = (0, 255, 0)
platform_x, platform_y = width // 2 - platform_width // 2, height - 50

# Set up camera
camera_x = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keys that are currently being held down
    keys = pygame.key.get_pressed()

    # Update player position based on keys
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed

    # Jumping mechanics
    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
    else:
        if jump_height >= -10:
            neg = 1
            if jump_height < 0:
                neg = -1
            player_y -= (jump_height ** 2) * 0.5 * neg
            jump_height -= 1
        else:
            jumping = False
            jump_height = 10

    # Scroll the camera based on player's movement
    camera_x = player_x - width // 2

    # Draw background
    screen.fill(white)

    # Draw platform relative to the camera position
    pygame.draw.rect(screen, platform_color, (platform_x - camera_x, platform_y, platform_width, platform_height))

    # Draw player relative to the camera position
    pygame.draw.rect(screen, player_color, (player_x - camera_x, player_y, player_size, player_size))

    # Update display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30)
