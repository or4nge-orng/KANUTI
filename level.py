import pygame
import settings
import random

NORTH, SOUTH, EAST, WEST = 'n', 's', 'e', 'w'

class Level:
    def __init__(self):
        self.map = {}
        self.map_size = 19
        for x in range(self.map_size):
            for y in range(self.map_size):
                self.map[(x, y)] = 1
                
        self.nextX = 0
        self.nextY = 0
        self.hasVisited = [(1, 1)]
        self.gen_maze(1, 1)

    def print_maze(self):
        for y in range(self.map_size):
            for x in range(self.map_size):
                print(self.map[(x, y)], end='')
            print()
        print()

    def draw_level(self, window):
        for coor in self.map:
            if self.map[coor] == 1:
                pygame.draw.rect(window, (255, 255, 255), (coor[0] * 50,
                                                           coor[1] * 50,
                                                           50 - 1,
                                                           50 - 1))
        
    def gen_maze(self, x, y):
        self.map[(x, y)] = 0

        while True:
            # Check which neighboring spaces adjacent to
            # the mark have not been visited already:
            unvisited_neighbors = []
            if y > 1 and (x, y - 2) not in self.hasVisited:
                unvisited_neighbors.append(NORTH)

            if y < self.map_size - 2 and (x, y + 2) not in self.hasVisited:
                unvisited_neighbors.append(SOUTH)

            if x > 1 and (x - 2, y) not in self.hasVisited:
                unvisited_neighbors.append(WEST)

            if x < self.map_size - 2 and (x + 2, y) not in self.hasVisited:
                unvisited_neighbors.append(EAST)

            if len(unvisited_neighbors) == 0:
                # BASE CASE
                # All neighboring spaces have been visited, so this is a
                # dead end. Backtrack to an earlier space:
                return
            else:
                # RECURSIVE CASE
                # Randomly pick an unvisited neighbor to visit:
                nextIntersection = random.choice(unvisited_neighbors)

                # Move the mark to an unvisited neighboring space:

                if nextIntersection == NORTH:
                    nextX = x
                    nextY = y - 2
                    self.map[(x, y - 1)] = 0  # Connecting hallway.
                elif nextIntersection == SOUTH:
                    nextX = x
                    nextY = y + 2
                    self.map[(x, y + 1)] = 0  # Connecting hallway.
                elif nextIntersection == WEST:
                    nextX = x - 2
                    nextY = y
                    self.map[(x - 1, y)] = 0  # Connecting hallway.
                elif nextIntersection == EAST:
                    nextX = x + 2
                    nextY = y
                    self.map[(x + 1, y)] = 0  # Connecting hallway.

                self.hasVisited.append((nextX, nextY))  # Mark as visited.
                self.gen_maze(nextX, nextY)  # Recursively visit this space.