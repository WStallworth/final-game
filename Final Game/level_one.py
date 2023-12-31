import pygame
from game_constants import *
import background
from swordsman import swordsmen
from object import HouseTiles,potion
import random
from fireball import fireballs
import sys
def level_one(hero):
    hero.weapon = 1
    hero.speed = PLAYER_SPEED
    #Init a screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Level One")

    #Creating a enemy sprites
    background.add_swordsmen(hero,5)

    #Creating Lives
    lives = NUM_LIVES
    hearts = pygame.image.load("assets/backgrounds/misc_sprites/heart.png").convert()
    hearts.set_colorkey((255,255,255))

    # Clock object
    clock = pygame.time.Clock()
    score = 0
    health_potions = 0

    #Adding score font
    score_font = pygame.font.Font("assets/fonts/Old London.ttf", 16)
    ability_font = pygame.font.Font("assets/fonts/BRIDGE.TTF", 16)
    ability_font_big = pygame.font.Font("assets/fonts/BRIDGE.TTF", 32)
    weapon_text = "Sword"
    arena = screen.copy()
    background.draw_level_one(arena)

    #Presenting abilities:
    screen.blit(arena,(0,0))
    ability_text1 = ability_font_big.render("New Ability: Melee Attack",True,(255,255,255))
    ability_text2 = ability_font_big.render("How to use: When within 5 tiles of an enemy if you click",True,(255,255,255))
    ability_text3 = ability_font_big.render("on them they will die and you will gain one point",True,(255,255,255))
    ability_text4 = ability_font_big.render("Left click to begin the level",True, (255,255,255))
    ability_text5 = ability_font_big.render("Press Q on the keyboard to access this ability", True, (255, 255, 255))
    screen.blit(ability_text1,(215,100))
    screen.blit(ability_text2,(32,132))
    screen.blit(ability_text3,(64,164))
    screen.blit(ability_text4,(215,196))
    screen.blit(ability_text5, (116, 228))
    pygame.display.flip()
    click = False
    while click != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
    #Main Loops
    while score < L1_WIN and lives > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            #Checking if you clicked on an enemy("Sword") and if they're in melee range(ONLY WORKS WHEN WEAPON IS 1)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and hero.weapon == 1:
                # Check if the mouse click is on any sprite in the group- CHAT GPT CODE
                clicked_sprites = [sprite for sprite in swordsmen if sprite.rect.collidepoint(event.pos)]
                for clicked_sprite in clicked_sprites:
                    if abs(clicked_sprite.rect.x-hero.rect.x) <= MELEE_RANGE and abs(clicked_sprite.rect.y-hero.rect.y) <= MELEE_RANGE:
                        clicked_sprite.kill()  # Remove the clicked sprite from the group
                        score += 1
                        background.add_swordsmen(hero,1)

        #THis begins drawing and checking things
        screen.blit(arena, (0, 0))

        #Updating things that move:
        hero.update()
        swordsmen.update()

        #Checking to ensure there is always 5 swoardsmen on the screen:
        if len(swordsmen) < 5:
            background.add_swordsmen(hero,(5-len(swordsmen)))

        #Randomly deciding if a potion should be dropped:
        health_chance = random.randint(0,50)
        if health_chance == 1 and health_potions == 0:
            potion.add(HouseTiles("assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0116.png",
                                  random.randint(BASETILE_SIZE, SCREEN_WIDTH - BASETILE_SIZE * 2),
                                  random.randint(BASETILE_SIZE, SCREEN_HEIGHT - BASETILE_SIZE * 2)))
            health_potions = 1

        # Drawing things
        hero.draw(screen)
        swordsmen.draw(screen)
        potion.draw(screen)

        # Track lives in lower left corner:
        for i in range(1,lives+1):
            screen.blit(hearts, (BASETILE_SIZE * i, SCREEN_HEIGHT - BASETILE_SIZE))

        #Checking to see if the melee unit hits the player, and taking life if it does hit
        result = pygame.sprite.spritecollide(hero, swordsmen, True)
        for i in result:
            lives -= ENEMY_DAMAGE


        #Checking to see if you picked up health potion
        result = pygame.sprite.spritecollide(hero,potion,True)
        if result:
            lives += HEALTH_POTION_EFFECT
            health_potions = 0

        #Displaying score:
        text = score_font.render(f"Score : {score}", True, (0,0,0))
        screen.blit(text, (SCREEN_WIDTH - BASETILE_SIZE * 5, 0))

        #Shwoing equiped ability:
        ability = ability_font.render(f"Ability: {weapon_text}", True, (0, 0, 0))
        screen.blit(ability, ((SCREEN_WIDTH /2)-(BASETILE_SIZE*2), 0))


        # Flipping the display so you can actually see
        pygame.display.flip()
        # Clock
        clock.tick(30)
    #Return at the end
    #This code removes all enemies so when you relaunch the level theres no pre-existing people
    for person in swordsmen:
        swordsmen.remove(person)
    hero.rect.x = SCREEN_WIDTH/2
    hero.rect.y = SCREEN_HEIGHT/2
    return score

