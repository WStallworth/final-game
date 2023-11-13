import pygame
from game_constants import *
# Drawing Houses
from object import HouseTiles, red_house, gray_house, decor
import random


def draw_spawn(surface):
    # Covering everything in Grass
    grass = pygame.image.load("assets/backgrounds/Tiles/tile_0001.png").convert()
    for x in range(0, SCREEN_WIDTH, BASETILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, BASETILE_SIZE):
            surface.blit(grass, (x, y))
    # Adding Wall Corners:
    tl_corner = pygame.image.load("assets/backgrounds/Tiles/tile_0096.png").convert()
    tr_corner = pygame.image.load("assets/backgrounds/Tiles/tile_0098.png").convert()
    bl_corner = pygame.image.load("assets/backgrounds/Tiles/tile_0120.png").convert()
    br_corner = pygame.image.load("assets/backgrounds/Tiles/tile_0122.png").convert()
    surface.blit(tl_corner, (0, 0))
    surface.blit(tr_corner, (SCREEN_WIDTH - BASETILE_SIZE, 0))
    surface.blit(bl_corner, (0, SCREEN_HEIGHT - BASETILE_SIZE))
    surface.blit(br_corner, (SCREEN_WIDTH - BASETILE_SIZE, SCREEN_HEIGHT - BASETILE_SIZE))
    # Adding walls:
    l_wall = pygame.image.load("assets/backgrounds/Tiles/tile_0108.png").convert()
    t_wall = pygame.image.load("assets/backgrounds/Tiles/tile_0097.png").convert()
    b_wall = pygame.image.load("assets/backgrounds/Tiles/tile_0121.png").convert()
    r_wall = pygame.image.load("assets/backgrounds/Tiles/tile_0110.png").convert()
    # Left wall
    for y in range(BASETILE_SIZE, SCREEN_HEIGHT - BASETILE_SIZE, BASETILE_SIZE):
        surface.blit(l_wall, (0, y))
    # Right wall
    for y in range(BASETILE_SIZE, SCREEN_HEIGHT - BASETILE_SIZE, BASETILE_SIZE):
        surface.blit(r_wall, (SCREEN_WIDTH - BASETILE_SIZE, y))
    # Top Wall:
    for x in range(BASETILE_SIZE, SCREEN_WIDTH - BASETILE_SIZE, BASETILE_SIZE):
        surface.blit(t_wall, (x, 0))
    # Top Wall:
    for x in range(BASETILE_SIZE, SCREEN_WIDTH - BASETILE_SIZE, BASETILE_SIZE):
        surface.blit(b_wall, (x, SCREEN_HEIGHT - BASETILE_SIZE))


def draw_red_house(surface, x, y):
    door = HouseTiles('assets/backgrounds/Tiles/tile_0074.png', x + (BASETILE_SIZE * 2), y + (BASETILE_SIZE * 2))
    l_wall = HouseTiles('assets/backgrounds/Tiles/tile_0072.png', x, y + (BASETILE_SIZE * 2))
    r_wall = HouseTiles('assets/backgrounds/Tiles/tile_0075.png', x + (BASETILE_SIZE * 3), y + (BASETILE_SIZE * 2))
    wall = HouseTiles('assets/backgrounds/Tiles/tile_0073.png', x + BASETILE_SIZE, y + (BASETILE_SIZE * 2))
    red_house.add(door, l_wall, r_wall, wall)
    # Roof pieces
    for i in range(4):
        red_house.add(HouseTiles("assets/backgrounds/Tiles/tile_0049.png", x + (i * BASETILE_SIZE), y))
        red_house.add(HouseTiles('assets/backgrounds/Tiles/tile_0061.png', x + (i * BASETILE_SIZE), y + BASETILE_SIZE))
    # Drawing Lower part of house:
    red_house.draw(surface)


def draw_gray_house(surface, x, y):
    door = HouseTiles('assets/backgrounds/Tiles/tile_0078.png', x + (BASETILE_SIZE * 2), y + (BASETILE_SIZE * 2))
    l_wall = HouseTiles('assets/backgrounds/Tiles/tile_0076.png', x, y + (BASETILE_SIZE * 2))
    r_wall = HouseTiles('assets/backgrounds/Tiles/tile_0079.png', x + (BASETILE_SIZE * 3), y + (BASETILE_SIZE * 2))
    wall = HouseTiles('assets/backgrounds/Tiles/tile_0077.png', x + BASETILE_SIZE, y + (BASETILE_SIZE * 2))
    gray_house.add(door, l_wall, r_wall, wall)
    # Roof pieces
    for i in range(4):
        gray_house.add(HouseTiles("assets/backgrounds/Tiles/tile_0053.png", x + (i * BASETILE_SIZE), y))
        gray_house.add(HouseTiles('assets/backgrounds/Tiles/tile_0065.png', x + (i * BASETILE_SIZE), y + BASETILE_SIZE))
    # Drawing Lower part of house:
    gray_house.draw(surface)


def make_plants():
    """This function creates plants, gives them a location, and adds them to the group"""
    for _ in range(random.randint(10, 20)):
        decor.add(HouseTiles("assets/backgrounds/Tiles/tile_0005.png", random.randint(BASETILE_SIZE, SCREEN_WIDTH - BASETILE_SIZE*2),
                  random.randint(BASETILE_SIZE, SCREEN_HEIGHT - BASETILE_SIZE*2)))
    for _ in range(random.randint(10, 20)):
        decor.add(HouseTiles("assets/backgrounds/Tiles/tile_0027.png", random.randint(BASETILE_SIZE, SCREEN_WIDTH - BASETILE_SIZE*2),
                  random.randint(BASETILE_SIZE, SCREEN_HEIGHT - BASETILE_SIZE*2)))
    for _ in range(random.randint(10, 20)):
        decor.add(HouseTiles("assets/backgrounds/Tiles/tile_0028.png", random.randint(BASETILE_SIZE, SCREEN_WIDTH - BASETILE_SIZE*2),
                  random.randint(BASETILE_SIZE, SCREEN_HEIGHT - BASETILE_SIZE*2)))
    for _ in range(random.randint(10, 20)):
        decor.add(HouseTiles("assets/backgrounds/Tiles/tile_0029.png", random.randint(BASETILE_SIZE, SCREEN_WIDTH - BASETILE_SIZE*2),
                  random.randint(BASETILE_SIZE, SCREEN_HEIGHT - BASETILE_SIZE*2)))

