import pygame
from math import sin, cos, pi
import settings, funcs


class Player:
    def __init__(self):
        self.dt = 0
        self.x = 150
        self.y = 150
        self.angle = 0
        self.dx = cos(self.angle) * 0.6
        self.dy = sin(self.angle) * 0.6
        self.collision = pygame.Rect(self.x, self.y, 50, 50)
        
    def draw_player(self, window):
        pygame.draw.circle(window, (255, 0, 0), (self.x, self.y), 10)
    
    def detect_collision_wall(self, dx, dy):
        y = int((self.y + dy) / settings.BLOCKSIZE)
        x = int((self.x + dx) / settings.BLOCKSIZE)
        
        if settings.level.map[(x, y)]:
            self.x += 0
            self.y += 0
        else:
            self.x += dx
            self.y += dy
            
        
    
    def move(self):
        if pygame.mouse.get_focused():
            da = pygame.mouse.get_rel()
            pygame.mouse.set_pos(settings.WIDTH / 2, settings.HEIGHT / 2)
            self.angle += da[0] * 0.15 * funcs.delta_time()
            if self.angle < 0:
                self.angle += 2 * pi
            if self.angle > 2 * pi:
                self.angle -= 2 * pi
            
        if pygame.key.get_pressed()[pygame.K_w]:
            self.dx = cos(self.angle) * funcs.delta_time() * settings.PLAYER_SPEED
            self.dy = sin(self.angle) * funcs.delta_time() * settings.PLAYER_SPEED
            self.detect_collision_wall(self.dx, self.dy)
            
        if pygame.key.get_pressed()[pygame.K_s]:
            self.dx = cos(self.angle + pi) * funcs.delta_time() * settings.PLAYER_SPEED
            self.dy = sin(self.angle + pi) * funcs.delta_time() * settings.PLAYER_SPEED
            self.detect_collision_wall(self.dx, self.dy)

            
        if pygame.key.get_pressed()[pygame.K_d]:  
            self.dx = cos(self.angle + pi / 2) * funcs.delta_time() * settings.PLAYER_SPEED
            self.dy = sin(self.angle + pi / 2) * funcs.delta_time() * settings.PLAYER_SPEED
            self.detect_collision_wall(self.dx, self.dy)
            
        if pygame.key.get_pressed()[pygame.K_a]:
            self.dx = cos(self.angle - pi / 2) * funcs.delta_time() * settings.PLAYER_SPEED
            self.dy = sin(self.angle - pi / 2) * funcs.delta_time() * settings.PLAYER_SPEED
            self.detect_collision_wall(self.dx, self.dy)