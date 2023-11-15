import pygame
import sys
from game_constants import *

def main(screen):

    # Set up display
    #screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Level Select")
    # Set up fonts
    font = pygame.font.Font("assets/fonts/Old London.ttf", 36)
    #Setting up button
    button_width, button_height = SCREEN_WIDTH//5, SCREEN_HEIGHT//5
    level_1_button_rect = pygame.Rect(0,0,button_width,SCREEN_HEIGHT)
    level_2_button_rect = pygame.Rect(SCREEN_WIDTH/5,0,button_width,SCREEN_HEIGHT)
    level_3_button_rect = pygame.Rect(SCREEN_WIDTH * (2/5), 0, button_width, SCREEN_HEIGHT)
    level_4_button_rect = pygame.Rect(SCREEN_WIDTH *(3/5), 0, button_width, SCREEN_HEIGHT)
    back_button_rect = pygame.Rect(SCREEN_WIDTH *(4/5), 0, button_width, SCREEN_HEIGHT)

    #Setting up snipets of each level for buttons:
    bronze = pygame.image.load("assets/backgrounds/bronze.jpg").convert()
    iron = pygame.image.load("assets/backgrounds/iron.jpg").convert()
    gold = pygame.image.load("assets/backgrounds/gold.jpg").convert()
    emerald = pygame.image.load("assets/backgrounds/emerald.jpg").convert()
    home = pygame.image.load("assets/backgrounds/home.png").convert()
    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()

                    # Checking which button the mouse hit
                    if level_1_button_rect.collidepoint(mouse_pos):
                        # Another function for the store
                        print("Level 1")

                    # Check if the mouse clicked on the "No" button
                    elif level_2_button_rect.collidepoint(mouse_pos):
                        print("Level 2")

                    elif level_3_button_rect.collidepoint(mouse_pos):
                        print("Level 3")

                    elif level_4_button_rect.collidepoint(mouse_pos):
                        print("Level 4")

                    elif back_button_rect.collidepoint(mouse_pos):
                        return None
        # Draw background
        screen.fill((255,255,255))
        screen.blit(bronze,(0,SCREEN_HEIGHT/2-80))
        screen.blit(iron,(SCREEN_WIDTH/5,SCREEN_HEIGHT/2-80))
        screen.blit(gold,(SCREEN_WIDTH * (2/5), SCREEN_HEIGHT/2-80))
        screen.blit(emerald,(SCREEN_WIDTH *(3/5), SCREEN_HEIGHT/2-80))
        screen.blit(home,(SCREEN_WIDTH *(4/5), SCREEN_HEIGHT/2-80))
        # Update display
        pygame.display.flip()

        # Control the frame rate
        pygame.time.Clock().tick(30)