#All of my imports(Will be a lot)
import pygame
import random
import sys
from background import draw_background, update_background
from game_constants import *
from player import Player

#Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("A Sick Title for the game")

#Clock object
clock = pygame.time.Clock()

#Main loop
running = True
background = screen.copy()
draw_background(background)

#Creating an instance of the player
#TODO: Actually fix the player class, this is just a skeleton to test with
hero = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,"Earth","assets/backgrounds/Tiles/tile_0003.png")
#These are my offset variables, used to work with scrolling.  Offsetting from center of screen
x_offset = 0
y_offset = 0
#Main Loop:
while running:
    #quit condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #This will be my movement code:
        hero.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hero.move_up()
            if event.key == pygame.K_DOWN:
                hero.move_down()
            if event.key == pygame.K_LEFT:
                hero.move_left()
            if event.key == pygame.K_RIGHT:
                hero.move_right()

    #Updating hero
    hero.update()
    x_offset = int(hero.x - SCREEN_WIDTH // 2)
    y_offset = int(hero.y - (SCREEN_HEIGHT // 2))
    # draw background and update
    update_background(background, x_offset, y_offset)
    hero.draw(background)
    screen.blit(background, (0, 0))

    #Flipping the display so you can actually see
    pygame.display.flip()
    #Clock
    clock.tick(60)
# quit pygame
pygame.quit()
sys.exit()