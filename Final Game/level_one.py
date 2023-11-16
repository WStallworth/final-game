import pygame
import sys
from game_constants import *
import background
def level_one(hero):
    #Init a screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Level One")

    # Clock object
    clock = pygame.time.Clock()
    score = 0
    arena = screen.copy()
    background.draw_level_one(arena)
    #Main Loops
    while score != L1_WIN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
                # This will be my movement code:
            hero.stop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    hero.move_up()
                    score+=1
                if event.key == pygame.K_DOWN:
                    hero.move_down()
                if event.key == pygame.K_LEFT:
                    hero.move_left()
                if event.key == pygame.K_RIGHT:
                    hero.move_right()
        screen.blit(arena, (0, 0))

        #Updating things that move:
        hero.update()
        #Drawing things that move
        hero.draw(screen)
        # Flipping the display so you can actually see
        pygame.display.flip()
        # Clock
        clock.tick(30)
    #Return at the end
    return score
