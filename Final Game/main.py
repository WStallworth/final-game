#All of my imports(Will be a lot)
import pygame
import random
import sys
from background import draw_spawn
from game_constants import *
from player import Player
import misc
import object
import store
#Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("A Sick Title for the game")

#Clock object
clock = pygame.time.Clock()

#Main loop
running = True
background = screen.copy()
misc.draw_spawn(background)
#make the plants and assign them positions and check to ensure that they aren't colliding
misc.make_plants()
#Creating an instance of the player
#TODO: Actually fix the player class, this is just a skeleton to test with
hero = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,"Earth","assets/backgrounds/Tiles/tile_0003.png")


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

    #Checking for house collisions:
    result = pygame.sprite.spritecollide(hero, object.red_house, False)
    if result != []:
        hero.stop()
        hero.x = SCREEN_WIDTH/2
        hero.y = SCREEN_HEIGHT/2
        #level_selection.main()

    result = pygame.sprite.spritecollide(hero, object.gray_house, False)
    if result != []:
        hero.stop()
        hero.x = SCREEN_WIDTH/2
        hero.y = SCREEN_HEIGHT/2
        store.main()

    #TODO: Make do you want to enter screen

    # draw background and update
    screen.blit(background, (0, 0))
    misc.draw_red_house(background, 150, 125)
    misc.draw_gray_house(background,600,450)
    object.decor.draw(screen)
    hero.update()
    hero.draw(screen)

    #TODO: Figure out a way so plants arent on buildings without ruining performance

    #Flipping the display so you can actually see
    pygame.display.flip()
    #Clock
    clock.tick(60)
# quit pygame
pygame.quit()
sys.exit()