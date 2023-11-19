import pygame
import sys
from game_constants import *
# Set up colors
#THIS IS ALL FROM CHAT GPT
def main(screen):

    # Initialize Pygame

    # Set up display
    #screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("How to Play")
    background_image = pygame.image.load("assets/backgrounds/htp_main.PNG")
    counter = 1
    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    counter += 1

        if counter == 2:
            background_image = pygame.image.load("assets/backgrounds/htp_lvl_select.PNG")

        elif counter == 3:
            background_image = pygame.image.load("assets/backgrounds/htp_lvl_ui.PNG")

        elif counter>= 4:
            return
        screen.blit(background_image,(0,0))

        # Update display
        pygame.display.flip()


