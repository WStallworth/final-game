import pygame
from game_constants import *
import random
from swordsman import Swordsman, swordsmen
from wizard import Wizard,wizards
from super_enemy import Super_Enemy, supers

def draw_level_four(surface):
    # Covering everything in dungeon floor
    floor = ["assets/backgrounds/Tiles/Colored/tile_0110.png",
             "assets/backgrounds/Tiles/Colored/tile_0111.png",
             "assets/backgrounds/Tiles/Colored/tile_0126.png",
             "assets/backgrounds/Tiles/Colored/tile_0127.png",
             "assets/backgrounds/Tiles/Colored/tile_0142.png",
             "assets/backgrounds/Tiles/Colored/tile_0143.png",
             "assets/backgrounds/Tiles/Colored/tile_0158.png",
             "assets/backgrounds/Tiles/Colored/tile_0159.png"]
    for x in range(0, SCREEN_WIDTH, BASETILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, BASETILE_SIZE):
            index = random.randint(0, 7)
            image = pygame.image.load(floor[index]).convert()
            image = pygame.transform.scale(image,(16,16))
            surface.blit(image, (x, y))
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
def draw_level_three(surface):
    # Covering everything in dungeon floor
    floor = ["assets/backgrounds/Tiles/tile_0000.png",
             "assets/backgrounds/Tiles/tile_0001.png",
             "assets/backgrounds/Tiles/tile_0002.png",
             "assets/backgrounds/Tiles/tile_0043.png"]
    for x in range(0, SCREEN_WIDTH, BASETILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, BASETILE_SIZE):
            index = random.randint(0, 3)
            surface.blit(pygame.image.load(floor[index]).convert(), (x, y))
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


def draw_level_two(surface):
    # Covering everything in dungeon floor
    floor = ["assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0000.png",
             "assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0012.png",
             "assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0024.png"]
    for x in range(0, SCREEN_WIDTH, BASETILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, BASETILE_SIZE):
            index = random.randint(0, 2)
            surface.blit(pygame.image.load(floor[index]).convert(), (x, y))
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

def draw_level_one(surface):
    # Covering everything in dungeon floor
    floor = ["assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0048.png",
             "assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0049.png",
             "assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0050.png",
             "assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0051.png",
             "assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0052.png",
             "assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0053.png",
             "assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0042.png"]
    for x in range(0, SCREEN_WIDTH, BASETILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, BASETILE_SIZE):
            index = random.randint(0, 6)
            surface.blit(pygame.image.load(floor[index]).convert(), (x, y))
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

def add_swordsmen(target,num):
    for _ in range(num):
        swordsmen.add(Swordsman(random.randint(BASETILE_SIZE, SCREEN_WIDTH - BASETILE_SIZE*2),
                                random.randint(BASETILE_SIZE, SCREEN_HEIGHT - BASETILE_SIZE*2),
                                "assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0109.png",target))

def add_wizards(target,num):
    for _ in range(num):
        wizards.add(Wizard(random.randint(BASETILE_SIZE, SCREEN_WIDTH - BASETILE_SIZE*2),
                                random.randint(BASETILE_SIZE, SCREEN_HEIGHT - BASETILE_SIZE*2),
                                "assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0084.png",target))

def add_super(target,num):
    for _ in range(num):
        supers.add(Super_Enemy(random.randint(BASETILE_SIZE, SCREEN_WIDTH - BASETILE_SIZE*2),
                                random.randint(BASETILE_SIZE, SCREEN_HEIGHT - BASETILE_SIZE*2),
                                "assets/backgrounds/kenney_tiny-dungeon/Tiles/tile_0111.png",target))



