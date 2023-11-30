import pygame
from game_constants import *
import background
from object import HouseTiles,wall,potion
import random
from fireball import Fireball,fireballs,enemy_fireballs
from super_enemy import supers
def level_four(hero):
    hero.weapon = 1
    hero.speed = PLAYER_SPEED
    #Init a screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Level Four")
    #This is code for my wall lifespan
    wall_life = 0
    #Creating a enemy sprites
    background.add_super(hero,10)
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
    background.draw_level_three(arena)
    # Presenting abilities:
    screen.blit(arena, (0, 0))
    ability_text1 = ability_font_big.render("New Ability: Wall Build", True, (255, 255, 255))
    ability_text2 = ability_font_big.render("How to use: Click and drag to create walls wherever", True,
                                            (255, 255, 255))
    ability_text3 = ability_font_big.render("you drag. If it hits an enemy you do NOT gain", True,
                                            (255, 255, 255))
    ability_text4 = ability_font_big.render("a point,but it will kill them and fireballs. Left click to begin", True, (255, 255, 255))
    ability_text5 = ability_font_big.render("Press 3 on the keyboard to access this ability", True, (255, 255, 255))
    screen.blit(ability_text1, (260, 100))
    screen.blit(ability_text2, (64, 132))
    screen.blit(ability_text3, (32, 164))
    screen.blit(ability_text4, (34, 196))
    screen.blit(ability_text5, (116, 228))
    pygame.display.flip()
    click = False
    while click != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
    #Main Loops
    while score < L4_WIN and lives > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            #Weapon Change:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    hero.weapon = 1
                elif event.key == pygame.K_2:
                    hero.weapon = 2
                elif event.key == pygame.K_3:
                    hero.weapon = 3
            #Checking if you clicked on an enemy("Sword") and if they're in melee range(ONLY WORKS WHEN WEAPON IS 1)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and hero.weapon == 1:
                # Check if the mouse click is on any sprite in the group- CHAT GPT CODE
                clicked_sprites = [sprite for sprite in supers if sprite.rect.collidepoint(event.pos)]
                for clicked_sprite in clicked_sprites:
                    if abs(clicked_sprite.rect.x-hero.rect.x) <= MELEE_RANGE and abs(clicked_sprite.rect.y-hero.rect.y) <= MELEE_RANGE:
                        clicked_sprite.kill()  # Remove the clicked sprite from the group
                        score += 1
                        background.add_super(hero,1)
            #This code is for weapon 2, fireball(or arrows, whichever I havea picture for)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and hero.weapon == 2:
                fireballs.add(Fireball("assets/backgrounds/misc_sprites/fireball.png",hero.rect.x,hero.rect.y,*event.pos))
            #This is code for weapon 3, defensive weapon
            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0] and hero.weapon == 3:
                # Create a new sprite while the left mouse button is pressed and mouse is moving
                wall.add(HouseTiles("assets/backgrounds/Tiles/tile_0126.png",*event.pos))

        #THis begins drawing and checking things
        screen.blit(arena, (0, 0))

        #Updating things that move:
        hero.update()
        supers.update()
        fireballs.update()
        enemy_fireballs.update()
        #Checking to ensure there is always 5 wizards on the screen:
        if len(supers) < 10:
            background.add_super(hero,(10-len(supers)))

        #Randomly deciding if each wizard will shoot a fireball
        for enemy in supers:
            chance = random.randint(0,FIREBALL_CHANCE)
            if chance == 1:
                enemy_fireballs.add(Fireball("assets/backgrounds/misc_sprites/fireball.png",enemy.rect.x,enemy.rect.y,
                                             hero.rect.x,hero.rect.y))

        for fireball in enemy_fireballs:
            fireball.speed = ENEMY_FIREBALL_SPEED
        #Randomly deciding if a potion should be dropped:
        health_chance = random.randint(0,50)
        if health_chance == 1 and health_potions == 0:
            potion.add(HouseTiles("assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0116.png",
                                  random.randint(BASETILE_SIZE, SCREEN_WIDTH - BASETILE_SIZE * 2),
                                  random.randint(BASETILE_SIZE, SCREEN_HEIGHT - BASETILE_SIZE * 2)))
            health_potions = 1

        # Drawing things
        hero.draw(screen)
        supers.draw(screen)
        wall.draw(screen)
        potion.draw(screen)
        fireballs.draw(screen)
        enemy_fireballs.draw(screen)

        # Track lives in lower left corner:
        for i in range(1,lives+1):
            screen.blit(hearts, (BASETILE_SIZE * i, SCREEN_HEIGHT - BASETILE_SIZE))

        #Checking to see if the wizard unit hits the player, and taking life if it does hit
        result = pygame.sprite.spritecollide(hero, supers, True)
        if result:
            lives -= len(result) * ENEMY_DAMAGE

        #Checking to see if the fireball hits the player:
        result = pygame.sprite.spritecollide(hero,enemy_fireballs,True)
        if result:
            lives -= len(result) * WIZARD_FIRE

        #Checking to see if bad guys run into the walls, if they do kill them(for now)
        pygame.sprite.groupcollide(supers, wall, False, True)

        #Checking to see if bad fireballs run into a wall:
        pygame.sprite.groupcollide(enemy_fireballs, wall, True, True)
        #Checking to see if you picked up health potion
        result = pygame.sprite.spritecollide(hero,potion,True)
        if result:
            lives += HEALTH_POTION_EFFECT
            health_potions = 0

        #Killing wizards if they get hit by fireball
        result = pygame.sprite.groupcollide(supers,fireballs,True,True)
        if result:
            score += len(result)
            background.add_wizards(hero,len(result))

        #Displaying score:
        text = score_font.render(f"Score : {score}", True, (0, 0, 0))
        screen.blit(text, (SCREEN_WIDTH - BASETILE_SIZE * 5, 0))

        #Shwoing equiped ability:
        if hero.weapon == 1:
            weapon_text = "Sword"
        elif hero.weapon == 2:
            weapon_text = "Fireball"
        elif hero.weapon == 3:
            weapon_text = "Wall Build"
        ability = ability_font.render(f"Ability: {weapon_text}", True, (0, 0, 0))
        screen.blit(ability, ((SCREEN_WIDTH /2)-(BASETILE_SIZE*2), 0))


        # Flipping the display so you can actually see
        pygame.display.flip()
        #removing walls eventually
        wall_life += 1
        if wall_life == WALL_LIFESPAN:
            for block in wall:
                wall.remove(block)
            wall_life = 0
        # Clock
        clock.tick(30)
    #Return at the end
    #This code removes all enemies so when you relaunch the level theres no pre-existing people
    for person in supers:
        supers.remove(person)
    for fireball in fireballs:
        fireballs.remove(fireball)
    hero.rect.x = SCREEN_WIDTH/2
    hero.rect.y = SCREEN_HEIGHT/2
    return score
