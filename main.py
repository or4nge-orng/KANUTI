import pygame
import sys
import pandas as pd

import settings
import funcs
import menus
import raycast
from player import Player

window_size = settings.WIDTH, settings.HEIGHT

pygame.init()

def main(level_num):
    window = pygame.display.set_mode(window_size)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('arial', 30, bold=True)
    level_txt = font.render(f'Level {level_num}', True, 'black')
    counter = 1
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 1000)
    print(level_num)
    level = settings.level
    player = Player()
    cur_level_points = 0
    while True:
        window.fill('black')
        player.dt = funcs.delta_time()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                if settings.player_records.loc[settings.username, 'record'] < settings.points + cur_level_points:
                    settings.player_records.loc[settings.username, 'record'] = settings.points + cur_level_points
                    settings.player_records.to_csv('data/players.csv', sep=';')
                pygame.quit()
                sys.exit()
                
            if event.type == timer_event: 
                print(counter, settings.points)
                cur_level_points = counter * 1000 * level_num
                counter += 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                settings.paused = True
        
        if funcs.check_player_finished(player):
            level.reset_level()
            settings.create_block_map()
            level_num += 1
            settings.points += cur_level_points
            if settings.player_records.loc[settings.username, 'record'] < settings.points:
                settings.player_records.loc[settings.username, 'record'] = settings.points
                settings.player_records.to_csv('data/players.csv', sep=';')
            print(settings.player_records.loc[settings.username, 'record'])
            menus.level_change_menu(window)
            main(level_num)

        if settings.paused:
            menus.pause_menu(window, cur_level_points)
        else:
            raycast.raycast(window, player)
            player.move()
            #settings.draw_level(window)
            #player.draw_player(window)
            
        pygame.draw.rect(window, 'white', level_txt.get_rect())    
        window.blit(level_txt, (0, 0))
        pygame.display.set_caption(f'FPS: {clock.get_fps()}')
        clock.tick(settings.FPS)
        pygame.display.update()


if __name__ == '__main__':
    menus.start_menu()
    main(level_num=1)
    