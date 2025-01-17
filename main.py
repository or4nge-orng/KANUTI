import pygame
import pygame_widgets
import sys

import pygame_widgets.button
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
    window.fill('white')
    player.dt = funcs.delta_time()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #level.draw_level(window)
    #player.draw_player(window)
    #player.move()
    start_btn = pygame_widgets.button.Button(window, 200, 300, 200, 50, text='Start', inactiveColour=(200, 50, 0))
    #raycast.raycast(window, player)
        
    clock.tick(settings.FPS)
    pygame_widgets.update(events)
    pygame.display.update()
