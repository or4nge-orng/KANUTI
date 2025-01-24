import pygame
import pygame_widgets
import sys
import pprint

import pygame_widgets.button
import settings
import funcs

import raycast
from level import Level
from player import Player

window_size = settings.WIDTH, settings.HEIGHT


def start_menu(window):
    btn_size = 200, 50
    menu_font = pygame.font.SysFont('arial', 30, bold=True)
    start_btn = pygame_widgets.button.Button(window, settings.WIDTH * 0.08, settings.HEIGHT * 0.77 - 80,
                                            *btn_size, text='Start',
                                            inactiveColour=(220, 220, 220), hoverColour=(180, 180, 180),
                                            radius=btn_size[0] // 10, font=menu_font)
    exit_btn = pygame_widgets.button.Button(window, settings.WIDTH * 0.08, settings.HEIGHT * 0.77,
                                            *btn_size, text='Exit',
                                            inactiveColour=(220, 220, 220), hoverColour=(180, 180, 180), 
                                            radius=btn_size[0] // 10, font=menu_font)
    while True:
        window.fill('black')
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        if start_btn.clicked:
            return
        
        if exit_btn.clicked:
            pygame.quit()
            sys.exit()
            
        pygame_widgets.update(events)
        pygame.display.update()


def main():
    pygame.init()
    window = pygame.display.set_mode(window_size)
    clock = pygame.time.Clock()
    start_menu(window)
    level = Level()
    pprint.pprint(level.map)
    player = Player()
    while True:
        window.fill('black')
        player.dt = funcs.delta_time()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        level.draw_level(window)
        #player.draw_player(window)
        raycast.raycast(window, player)
        player.move()
        clock.tick(settings.FPS)
        pygame.display.update()

if __name__ == '__main__':
    main()
    