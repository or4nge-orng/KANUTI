import pygame
import sys

import settings
import funcs
import start_menu
import raycast
from player import Player

window_size = settings.WIDTH, settings.HEIGHT


def main():
    pygame.init()
    window = pygame.display.set_mode(window_size)
    clock = pygame.time.Clock()
    start_menu.start_menu(window)
    level = settings.level
    player = Player()
    while True:
        window.fill('black')
        player.dt = funcs.delta_time()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #if event.type

        raycast.raycast(window, player)
        player.move()
        #player.draw_player(window)
        #settings.draw_level(window)
        
        pygame.display.set_caption(f'FPS: {clock.get_fps()}')
        clock.tick(settings.FPS)
        pygame.display.update()


if __name__ == '__main__':
    main()
    