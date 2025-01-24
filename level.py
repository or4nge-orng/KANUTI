import pygame
import settings
import labyrinth


class Level:
    def __init__(self):
        self.map = ['11111111111',
                    '10000000001',
                    '10000000001',
                    '10000000001',
                    '10000000001',
                    '10000000001',
                    '10000000001',
                    '10000000001',
                    '10000000001',
                    '11111111111']
        self.map_size = 11
        #for x in range(self.map_size):
        #    for y in range(self.map_size):
        #        self.map[(x, y)] = 1
                
        self.nextX = 0
        self.nextY = 0
        
    def print(self):
        for y in range(self.map_size):
            for x in range(self.map_size):
                print(self.map[(x, y)], end='')
            print() 

    def draw_level(self, window):
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] == '1':
                    pygame.draw.rect(window, (255, 255, 255), (col * settings.BLOCKSIZE,
                                                               row * settings.BLOCKSIZE,
                                                               settings.BLOCKSIZE - 1,
                                                               settings.BLOCKSIZE - 1))
        
    def gen_maze(self, x, y):
        pass