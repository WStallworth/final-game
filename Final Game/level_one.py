import pygame
import sys
from game_constants import *
import background
from swordsman import Swordsman,swordsmen
def level_one(hero):
    #Init a screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Level One")

    #Creating a enemy sprite
    background.draw_swordsmen(screen,hero)

    #Creating Lives
    lives = NUM_LIVES
    hearts = pygame.image.load("assets/backgrounds/misc_sprites/heart.png").convert()
    hearts.set_colorkey((255,255,255))
    # Clock object
    clock = pygame.time.Clock()
    score = 0
    arena = screen.copy()
    background.draw_level_one(arena)
    #Main Loops
    while score != L1_WIN and lives >0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            #Checking if you clicked on an enemy("Sword") and if they're in melee range
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Check if the mouse click is on any sprite in the group
                clicked_sprites = [sprite for sprite in swordsmen if sprite.rect.collidepoint(event.pos)]
                for clicked_sprite in clicked_sprites:
                    if abs(clicked_sprite.rect.x-hero.x) <= MELEE_RANGE and abs(clicked_sprite.rect.y-hero.y) <= MELEE_RANGE:
                        clicked_sprite.kill()  # Remove the clicked sprite from the group
                        score += 1
            # This will be my movement code checks to see if you pushed a key down, and will move unil that key goes up:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    hero.move_up()
                    score+=1
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
        #Drawing things that move
        hero.draw(screen)
        swordsmen.draw(screen)

        # Track lives in lower left corner:
        for i in range(1,lives+1):
            screen.blit(hearts, (BASETILE_SIZE * i, SCREEN_HEIGHT - BASETILE_SIZE))

        #Checking to see if the melee unit hits the player, and taking life if it does hit
        result = pygame.sprite.spritecollide(hero, swordsmen, True)
        for i in result:
            lives -= 1
        # Flipping the display so you can actually see
        pygame.display.flip()
        # Clock
        clock.tick(30)
    #Return at the end
    for person in swordsmen:
        swordsmen.remove(person)
    return score

