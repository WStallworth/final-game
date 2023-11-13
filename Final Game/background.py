import pygame
from game_constants import *

def draw_spawn(surface):
    #Covering everything in Grass
    grass = pygame.image.load("assets/backgrounds/Tiles/tile_0001.png").convert()
    for x in range(0,SCREEN_WIDTH,BASETILE_SIZE):
        for y in range(0,SCREEN_HEIGHT,BASETILE_SIZE):
            surface.blit(grass,(x,y))
    #Adding Wall Corners:
    tl_corner = pygame.image.load("assets/backgrounds/Tiles/tile_0096.png").convert()
    tr_corner = pygame.image.load("assets/backgrounds/Tiles/tile_0098.png").convert()
    bl_corner = pygame.image.load("assets/backgrounds/Tiles/tile_0120.png").convert()
    br_corner = pygame.image.load("assets/backgrounds/Tiles/tile_0122.png").convert()
    surface.blit(tl_corner,(0,0))
    surface.blit(tr_corner,(SCREEN_WIDTH-BASETILE_SIZE,0))
    surface.blit(bl_corner,(0,SCREEN_HEIGHT-BASETILE_SIZE))
    surface.blit(br_corner,(SCREEN_WIDTH-BASETILE_SIZE,SCREEN_HEIGHT-BASETILE_SIZE))
    #Adding walls:
    l_wall = pygame.image.load("assets/backgrounds/Tiles/tile_0108.png").convert()
    t_wall = pygame.image.load("assets/backgrounds/Tiles/tile_0097.png").convert()
    b_wall = pygame.image.load("assets/backgrounds/Tiles/tile_0121.png").convert()
    r_wall = pygame.image.load("assets/backgrounds/Tiles/tile_0110.png").convert()
    #Left wall
    for y in range(BASETILE_SIZE,SCREEN_HEIGHT-BASETILE_SIZE,BASETILE_SIZE):
        surface.blit(l_wall,(0,y))
    #Right wall
    for y in range(BASETILE_SIZE, SCREEN_HEIGHT - BASETILE_SIZE, BASETILE_SIZE):
        surface.blit(r_wall, (SCREEN_WIDTH-BASETILE_SIZE, y))
    #Top Wall:
    for x in range(BASETILE_SIZE,SCREEN_WIDTH-BASETILE_SIZE,BASETILE_SIZE):
        surface.blit(t_wall,(x,0))
    # Top Wall:
    for x in range(BASETILE_SIZE, SCREEN_WIDTH - BASETILE_SIZE, BASETILE_SIZE):
        surface.blit(b_wall, (x, SCREEN_HEIGHT-BASETILE_SIZE))




