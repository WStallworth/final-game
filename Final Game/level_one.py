import pygame
from game_constants import *
import background
from swordsman import swordsmen
from object import HouseTiles,wall,potion
import random
from fireball import Fireball,fireballs
def level_one(hero):
    #Init a screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Level One")
    #This is code for my wall lifespan
    wall_life = 0
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
    weapon_text = "Sword"
    arena = screen.copy()
    background.draw_level_one(arena)
    #Main Loops
    #TODO: TURN OFF GOD MODE: and lives > 0
    while score != L1_WIN:
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
                # Check if the mouse click is on any sprite in the group
                clicked_sprites = [sprite for sprite in swordsmen if sprite.rect.collidepoint(event.pos)]
                for clicked_sprite in clicked_sprites:
                    if abs(clicked_sprite.rect.x-hero.x) <= MELEE_RANGE and abs(clicked_sprite.rect.y-hero.y) <= MELEE_RANGE:
                        clicked_sprite.kill()  # Remove the clicked sprite from the group
                        score += 1
                        background.add_swordsmen(hero,1)
            #This code is for weapon 3, fireball(or arrows, whichever I havea picture for)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and hero.weapon == 2:
                fireballs.add(Fireball("assets/backgrounds/misc_sprites/fireball.png",hero.x,hero.y,*event.pos))
            #This is code for weapon 3, defensive weapon
            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0] and hero.weapon == 3:
                # Create a new sprite while the left mouse button is pressed and mouse is moving
                wall.add(HouseTiles("assets/backgrounds/Tiles/tile_0126.png",*event.pos))
            # This will be my movement code checks to see if you pushed a key down, and will move unil that key goes up:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    hero.move_up()
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    hero.move_left()
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    hero.move_down()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    hero.move_right()
            #Checks to see if the key goes up
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    hero.stop_y()
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    hero.stop_x()
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    hero.stop_y()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    hero.stop_x()

        screen.blit(arena, (0, 0))

        #Updating things that move:
        hero.update()
        swordsmen.update()
        fireballs.update()
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
        wall.draw(screen)
        potion.draw(screen)
        fireballs.draw(screen)
        # Track lives in lower left corner:
        for i in range(1,lives+1):
            screen.blit(hearts, (BASETILE_SIZE * i, SCREEN_HEIGHT - BASETILE_SIZE))

        #Checking to see if the melee unit hits the player, and taking life if it does hit
        result = pygame.sprite.spritecollide(hero, swordsmen, True)
        for i in result:
            lives -= ENEMY_DAMAGE

        #Checking to see if bad guys run into the walls, if they do kill them(for now)
        result = pygame.sprite.groupcollide(swordsmen, wall, True, False)
        if result:
            background.add_swordsmen(hero, len(result))

        #Checking to see if you picked up health potion
        result = pygame.sprite.spritecollide(hero,potion,True)
        if result:
            lives += HEALTH_POTION_EFFECT
            health_potions = 0

        result = pygame.sprite.groupcollide(swordsmen,fireballs,True,True)
        if result:
            score += len(result)
            background.add_swordsmen(hero,len(result))

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
    for person in swordsmen:
        swordsmen.remove(person)
    return score

