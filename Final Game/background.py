import pygame
from game_constants import *
def draw_background(surface):
    grass = pygame.image.load("assets/backgrounds/Tiles/tile_0001.png").convert()
    path = pygame.image.load("assets/backgrounds/Tiles/tile_0025.png").convert()
    #for now I'm just going to fill screen with grass and then another thing to the left of it to test
    #Drawing the main screen with just grass rn:
    for x in range(0,SCREEN_WIDTH,BASETILE_SIZE):
        for y in range(0,SCREEN_HEIGHT,BASETILE_SIZE):
            surface.blit(grass,(x,y))

    #This is drawing the path to the right of the grass:
    for x in range(SCREEN_WIDTH,2*SCREEN_WIDTH,BASETILE_SIZE):
        for y in range(0,SCREEN_HEIGHT,BASETILE_SIZE):
            surface.blit(path,(x,y))

def update_background(surface,x_offset,y_offset):
    grass = pygame.image.load("assets/backgrounds/Tiles/tile_0001.png").convert()
    path = pygame.image.load("assets/backgrounds/Tiles/tile_0025.png").convert()
    #TODO: Comment what this code is doing:
    for x in range(-x_offset,(SCREEN_WIDTH-x_offset),BASETILE_SIZE):
        for y in range(-y_offset,(SCREEN_HEIGHT-y_offset),BASETILE_SIZE):
            surface.blit(grass, (x, y))

    #TODO: Same here:
    for x in range(SCREEN_WIDTH-x_offset,SCREEN_WIDTH,BASETILE_SIZE):
        #TODO: Make y universal
        for y in range(0, SCREEN_HEIGHT, BASETILE_SIZE):
            surface.blit(path, (x, y))