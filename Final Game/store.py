import pygame
import sys
from game_constants import *
# Set up colors
#THIS IS ALL FROM CHAT GPT
def main():

    # Initialize Pygame
    pygame.init()

    # Set up display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Store Entrance Confirmation")
    background_image = pygame.image.load("assets/backgrounds/store.png")
    # Set up colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    red = (255, 0, 0)

    # Set up fonts
    font = pygame.font.Font("assets/fonts/Old London.ttf", 36)

    # Set up buttons
    button_width, button_height = 150, 50
    yes_button_rect = pygame.Rect(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2, button_width, button_height)
    no_button_rect = pygame.Rect((SCREEN_WIDTH // 4) * 3 - button_width, SCREEN_HEIGHT // 2, button_width, button_height)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()

                    # Check if the mouse clicked on the "Yes" button
                    if yes_button_rect.collidepoint(mouse_pos):
                        #Another function for the store
                        print("Hey")

                    # Check if the mouse clicked on the "No" button
                    elif no_button_rect.collidepoint(mouse_pos):
                        return None
                        # Add your logic for not entering the store

        # Draw background
        screen.blit(background_image,(0,0))

        # Draw buttons
        pygame.draw.rect(screen, green, yes_button_rect)
        pygame.draw.rect(screen, red, no_button_rect)

        # Draw text on buttons
        question = font.render("Do you want to enter the store?", True, white)
        yes_text = font.render("Yes", True, black)
        no_text = font.render("No", True, black)
        screen.blit(yes_text, (yes_button_rect.x + 50, yes_button_rect.y + 15))
        screen.blit(no_text, (no_button_rect.x + 60, no_button_rect.y + 15))
        screen.blit(question,(yes_button_rect.x+20,SCREEN_HEIGHT-400))

        # Update display
        pygame.display.flip()

        # Control the frame rate
        pygame.time.Clock().tick(30)

