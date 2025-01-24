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

block_map = set()
collisions = []

yBlock = 0
for i in Level().map:
    xBlock = 0
    for j in i:
        if j == '1':
            block_map.add((xBlock, yBlock))
            collisions.append(pygame.Rect(xBlock, yBlock, BLOCKSIZE, BLOCKSIZE))
        xBlock += BLOCKSIZE
    yBlock += BLOCKSIZE