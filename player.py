import pygame
from math import sin, cos, pi
import settings, funcs, copy


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
        pygame.draw.circle(window, (255, 0, 0), (self.x // 2, self.y // 2), 10)
        pygame.draw.line(window, (255, 0, 0), (self.x // 2, self.y // 2), (self.x + self.dx * 50, self.y + self.dy * 50), 5)
    
    def detect_collision_wall(self, dx, dy):
        next_rect = copy.copy(self.collision)
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(settings.collisions)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = settings.collisions[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top
            if abs(delta_x - delta_y) < 50:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0

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
            self.dx = cos(self.angle) * funcs.delta_time() * settings.PLAYER_SPEED
            self.dy = sin(self.angle) * funcs.delta_time() * settings.PLAYER_SPEED
            self.detect_collision_wall(-self.dx, -self.dy)
            
        if pygame.key.get_pressed()[pygame.K_a]:  
            self.dx = cos(self.angle + pi / 2) * funcs.delta_time() * settings.PLAYER_SPEED
            self.dy = sin(self.angle + pi / 2) * funcs.delta_time() * settings.PLAYER_SPEED
            self.detect_collision_wall(-self.dx, -self.dy)
            
        if pygame.key.get_pressed()[pygame.K_d]:
            self.dx = cos(self.angle - pi / 2) * funcs.delta_time() * settings.PLAYER_SPEED
            self.dy = sin(self.angle - pi / 2) * funcs.delta_time() * settings.PLAYER_SPEED
            self.detect_collision_wall(-self.dx, -self.dy)