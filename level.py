import settings
import random

NORTH, SOUTH, EAST, WEST = 'n', 's', 'e', 'w'

class Level:
    def __init__(self):
        self.map = {}
        self.map_size = settings.MAP_SIZE
        for x in range(self.map_size):
            for y in range(self.map_size):
                self.map[(x, y)] = 1
                
        self.nextX = 0
        self.nextY = 0
        self.hasVisited = [(1, 1)]
        self.gen_maze(1, 1)

        
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
                    self.nextX = x
                    self.nextY = y - 2
                    self.map[(x, y - 1)] = 0  # Connecting hallway.
                elif nextIntersection == SOUTH:
                    self.nextX = x
                    self.nextY = y + 2
                    self.map[(x, y + 1)] = 0  # Connecting hallway.
                elif nextIntersection == WEST:
                    self.nextX = x - 2
                    self.nextY = y
                    self.map[(x - 1, y)] = 0  # Connecting hallway.
                elif nextIntersection == EAST:
                    self.nextX = x + 2
                    self.nextY = y
                    self.map[(x + 1, y)] = 0  # Connecting hallway.

                self.hasVisited.append((self.nextX, self.nextY))  # Mark as visited.
                self.gen_maze(self.nextX, self.nextY)  # Recursively visit this space.
              
    def reset_level(self):
        self.map = {}
        self.map_size = settings.MAP_SIZE
        settings.block_map = set()
        for x in range(self.map_size):
            for y in range(self.map_size):
                self.map[(x, y)] = 1
                
        self.nextX = 0
        self.nextY = 0
        self.hasVisited = [(1, 1)]
        self.gen_maze(1, 1)
        
        