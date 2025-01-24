from math import pi
from level import Level
import pygame

FPS = 120
WIDTH = 1600
HEIGHT = 900
BLOCKSIZE = 100
RAY_NUM = 400
MAP_SIZE = 11
DEPTH_NUM = MAP_SIZE * BLOCKSIZE

PLAYER_SPEED = 1000
FOV = pi / 2
HALF_FOV = FOV / 2
dr = FOV / (RAY_NUM - 1)
level = Level()

block_map = set()
collisions = []

for coor in level.map:
    if level.map[coor] == 1:
        block_map.add((coor[0] * BLOCKSIZE, coor[1] * BLOCKSIZE))


def draw_level(window):
    for coor in block_map:
        if level.map[(coor[0] // 100, coor[1] // 100)] == 1:
            pygame.draw.rect(window, (255, 255, 255), (coor[0] // 2,
                                                       coor[1] // 2,
                                                       50 - 1,
                                                       50 - 1))