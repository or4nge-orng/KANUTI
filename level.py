import pygame
import settings


class Level:
    def __init__(self):
        self.map = {}
        for x in settings.MAP_SIZE:
            for y in settings.MAP_SIZE:
                self.map[(x, y)] = 1
        
    def gen_maze(self, window):
        pass