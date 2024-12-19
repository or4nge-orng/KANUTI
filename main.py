import pygame
import sys
import settings
import funcs

import raycast
from level import Level
from player import Player

window_size = settings.WIDTH, settings.HEIGHT

pygame.init()
window = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
level = Level()
player = Player()

while True:
    window.fill('black')
    player.dt = funcs.delta_time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #level.draw_level(window)
    #player.draw_player(window)
    player.move()
    raycast.raycast(window, player)
    
    clock.tick(settings.FPS)
    pygame.display.update()
