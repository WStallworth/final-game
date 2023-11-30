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
import level_one, level_two, level_three, level_four
#Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Gem Quest")

#Clock object
clock = pygame.time.Clock()

#These are initial values for ores:
bronze = 0
iron = 0
gold = 0
emerald = 0
play_again = False
#Pictures for ores to pull from later:
bronze_pic = pygame.image.load("assets/backgrounds/misc_sprites/bronze.jpg").convert()
iron_pic = pygame.image.load("assets/backgrounds/misc_sprites/iron.jpg").convert()
gold_pic = pygame.image.load("assets/backgrounds/misc_sprites/gold.jpg").convert()
emerald_pic = pygame.image.load("assets/backgrounds/misc_sprites/emerald.jpg").convert()
bronze_pic.set_colorkey((255,255,255))
iron_pic.set_colorkey((255,255,255))
gold_pic.set_colorkey((255,255,255))
emerald_pic.set_colorkey((255,255,255))
#Main loop
running = True
background = screen.copy()
misc.draw_spawn(background)
#make the plants and assign them positions and check to ensure that they aren't colliding
misc.make_plants()
#Creating an instance of the player
#TODO: Actually fix the player class, this is just a skeleton to test with
hero = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,1,"assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0088.png")
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


    #Checking for house collisions:
    result = pygame.sprite.spritecollide(hero, object.red_house, False)
    if result:
        #hero.stop()
        hero.rect.x = SCREEN_WIDTH/2
        hero.rect.y = SCREEN_HEIGHT/2
        level = level_selection.main(screen)
        if level == "L1":
            bronze = level_one.level_one(hero)
        elif level == "L2" and bronze:
            iron = level_two.level_two(hero)
        elif level == "L3" and iron:
            gold = level_three.level_three(hero)
        elif level == "L4" and gold:
            emerald = level_four.level_four(hero)


    #Second house collision
    result = pygame.sprite.spritecollide(hero, object.gray_house, False)
    if result:
        #hero.stop()
        hero.rect.x = SCREEN_WIDTH/2
        hero.rect.y = SCREEN_HEIGHT/2
        store.main(screen)

    hero.speed = 12
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

    #Drawing win icons in corner to track progress:
    if bronze >= L1_WIN:
        screen.blit(bronze_pic,(BASETILE_SIZE,SCREEN_HEIGHT-BASETILE_SIZE))
    if iron >= L2_WIN:
        screen.blit(iron_pic,(BASETILE_SIZE*2,SCREEN_HEIGHT-BASETILE_SIZE))
    if gold >= L3_WIN:
        screen.blit(gold_pic,(BASETILE_SIZE*3,SCREEN_HEIGHT-BASETILE_SIZE))
    if emerald >= L4_WIN:
        screen.blit(emerald_pic,(BASETILE_SIZE*4,SCREEN_HEIGHT-BASETILE_SIZE))
        play_again = False

    #Play again code
    if emerald >= L4_WIN and play_again == False:
        font = pygame.font.Font("assets/fonts/Old London.ttf", 36)
        green = (0, 255, 0)
        white = (255,255,255)
        black = (0,0,0)
        red = (255, 0, 0)
        background_image = pygame.image.load("assets/backgrounds/win.jpg")
        button_width, button_height = 150, 50
        yes_button_rect = pygame.Rect(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2, button_width, button_height)
        no_button_rect = pygame.Rect((SCREEN_WIDTH // 4) * 3 - button_width, SCREEN_HEIGHT // 2, button_width,
                                     button_height)
        pygame.display.flip()
        click = False
        while click != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        mouse_pos = pygame.mouse.get_pos()
                        # Check if the mouse clicked on the "Yes" button
                        if yes_button_rect.collidepoint(mouse_pos):
                            bronze = 0
                            iron = 0
                            gold = 0
                            emerald = 0
                            play_again = True
                            click = True
                        # Check if the mouse clicked on the "No" button
                        elif no_button_rect.collidepoint(mouse_pos):
                            sys.exit()
            pygame.draw.rect(screen, green, yes_button_rect)
            pygame.draw.rect(screen, red, no_button_rect)

            # Draw text on buttons
            screen.blit(background_image,(0,0))
            question = font.render("Do you want to play again?", True, black)
            yes_text = font.render("Yes", True, black)
            no_text = font.render("No", True, black)
            screen.blit(yes_text, (yes_button_rect.x + 50, yes_button_rect.y + 15))
            screen.blit(no_text, (no_button_rect.x + 60, no_button_rect.y + 15))
            screen.blit(question, (yes_button_rect.x + 20, SCREEN_HEIGHT - 400))
            # Update display
            pygame.display.flip()
    #TODO: Figure out a way so plants arent on buildings without ruining performance
    pygame.sprite.groupcollide(object.decor, object.gray_house, True,False)
    pygame.sprite.groupcollide(object.decor, object.red_house, True, False)
    #Flipping the display so you can actually see
    pygame.display.flip()
    #Clock
    clock.tick(30)
# quit pygame
pygame.quit()
sys.exit()