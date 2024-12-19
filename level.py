import pygame
import settings



class Level:
    def __init__(self):
        self.map = ['11111111',
                    '10000001',
                    '10000001',
                    '10011001',
                    '10010001',
                    '10000001',
                    '10000001',
                    '11111111']
        
    def draw_level(self, window):
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] == '1':
                    pygame.draw.rect(window, (255, 255, 255), (col * settings.BLOCKSIZE,
                                                               row * settings.BLOCKSIZE,
                                                               settings.BLOCKSIZE - 1,
                                                               settings.BLOCKSIZE - 1))