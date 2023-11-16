#All of my imports(Will be a lot)
import pygame
import random
import sys
from game_constants import *
from player import Player
import misc
import object
import store
import level_selection
from npc import NPC, NPCS
import level_one
from background import draw_level_one
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
hero = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,"Earth","assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0088.png")
#making npcs, and randomly generating their appearance
npc_images = ["assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0084.png","assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0085.png","assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0086.png","assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0099.png","assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0100.png"]
for _ in range(5):
    image = random.randint(0,4)
    NPCS.add(NPC(random.randint(BASETILE_SIZE, SCREEN_WIDTH - BASETILE_SIZE*2),random.randint(BASETILE_SIZE, SCREEN_HEIGHT - BASETILE_SIZE*2),npc_images[image]))
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
        level = level_selection.main(screen)
        if level == "L1":
            gold = level_one.level_one(hero)
    #Second house collision
    result = pygame.sprite.spritecollide(hero, object.gray_house, False)
    if result != []:
        hero.stop()
        hero.x = SCREEN_WIDTH/2
        hero.y = SCREEN_HEIGHT/2
        store.main(screen)

    #TODO: Make do you want to enter screen

    # draw background and update
    screen.blit(background, (0, 0))
    #These lines draw my houses and foliage
    misc.draw_red_house(background, 150, 125)
    misc.draw_gray_house(background,600,450)
    object.decor.draw(screen)
    #Updates things that are moving
    hero.update()
    NPCS.update()
    #Finally drawing things that are moving
    hero.draw(screen)
    NPCS.draw(screen)
    #TODO: Figure out a way so plants arent on buildings without ruining performance

    #Flipping the display so you can actually see
    pygame.display.flip()
    #Clock
    #TODO: ThIS IS A TEST

    clock.tick(30)
# quit pygame
pygame.quit()
sys.exit()