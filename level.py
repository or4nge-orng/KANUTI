import settings
import random


class Level:
    def __init__(self):
        self.map = {}
        self.map_size = 11
        for x in range(self.map_size):
            for y in range(self.map_size):
                self.map[(x, y)] = 1
                
        self.nextX = 0
        self.nextY = 0
        
    def print(self):
        for y in range(self.map_size):
            for x in range(self.map_size):
                print(self.map[(x, y)], end='')
            print() 

            
        
    def gen_maze(self, x, y):
        pass
