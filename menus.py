import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
import sys
import pandas as pd

import settings
    

btn_size = 200, 50

def set_username_check():
    global name_input
    settings.username = name_input.getText()


def check_username(username):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN] and username in settings.player_records.index and username:
        return True
    elif keys[pygame.K_RETURN] and username not in settings.player_records.index and username:
        settings.player_records.loc[username] = [0]
        settings.player_records.to_csv('data/players.csv', sep=';')
        return False



def start_menu():
    menu_font = pygame.font.SysFont('arial', 30, bold=True)
    window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    
    
    start_btn = Button(window, settings.WIDTH * 0.08, settings.HEIGHT * 0.77 - 80,
                                            *btn_size, text='Start',
                                            inactiveColour=(220, 220, 220), hoverColour=(180, 180, 180),
                                            radius=btn_size[0] // 10, font=menu_font)

    exit_btn = Button(window, settings.WIDTH * 0.08, settings.HEIGHT * 0.77,
                                            *btn_size, text='Exit',
                                            inactiveColour=(220, 220, 220), hoverColour=(180, 180, 180), 
                                            radius=btn_size[0] // 10, font=menu_font)
    while True:
        window.fill('black')
        events = pygame.event.get()
        if start_btn.clicked:
            global name_input
            name_input = TextBox(window, settings.WIDTH // 2 - 200, settings.HEIGHT // 2, 400, 50, fontSize=30, onSubmit=set_username_check)
            
        if check_username(settings.username):
            return
            
        if exit_btn.clicked:
            pygame.quit()
            sys.exit()
            
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()                                         
            
        pygame_widgets.update(events)
        pygame.display.update()
        

def pause_menu(window, cur_level_points):
    menu_font = pygame.font.SysFont('arial', 30, bold=True)
    if 'name_input' in globals():
        global name_input
        del name_input
    resume_btn = Button(window, settings.WIDTH * 0.08, settings.HEIGHT * 0.77 - 80,
                        *btn_size, text='Resume',
                        inactiveColour=(220, 220, 220), hoverColour=(180, 180, 180),
                        radius=btn_size[0] // 10, font=menu_font)
    exit_btn = Button(window, settings.WIDTH * 0.08, settings.HEIGHT * 0.77,
                        *btn_size, text='Exit',
                        inactiveColour=(220, 220, 220), hoverColour=(180, 180, 180), 
                        radius=btn_size[0] // 10, font=menu_font)
    while True:
        window.fill('black')
        events = pygame.event.get()
        if resume_btn.clicked:
            settings.paused = False
            return
        if exit_btn.clicked:
            if settings.player_records.loc[settings.username, 'record'] < settings.points + cur_level_points:
                settings.player_records.loc[settings.username, 'record'] = settings.points + cur_level_points
                settings.player_records.to_csv('data/players.csv', sep=';')
            pygame.quit()
            sys.exit()
        for event in events:
            if event.type == pygame.QUIT:
                if settings.player_records.loc[settings.username, 'record'] < settings.points + cur_level_points:
                    settings.player_records.loc[settings.username, 'record'] = settings.points + cur_level_points
                    settings.player_records.to_csv('data/players.csv', sep=';')
                pygame.quit()
                sys.exit()   
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                settings.paused = False
                return    
            
        pygame_widgets.update(events)
        pygame.display.update()                                 
            
        
        
def level_change_menu(window):
    if 'name_input' in globals():
        global name_input
        del name_input
    menu_font = pygame.font.SysFont('arial', 30, bold=True)
    exit_btn = Button(window, settings.WIDTH // 2 - btn_size[0] // 2, settings.HEIGHT * 0.8,
                        *btn_size, text='Exit', inactiveColour=(220, 220, 220), hoverColour=(180, 180, 180), 
                        radius=btn_size[0] // 10, font=menu_font)
    continue_txt = menu_font.render('To continue press SPACE', True, (255, 255, 255))
    score_txt = menu_font.render('Score: ' + str(settings.points), True, (255, 255, 255))
    record_txt = menu_font.render('Record: ' + str(settings.player_records.loc[settings.username, 'record']), True, (255, 255, 255))
    while True:
        window.fill('black')
        events = pygame.event.get()
        if exit_btn.clicked:
            if settings.player_records.loc[settings.username, 'record'] < settings.points:
                settings.player_records.loc[settings.username, 'record'] = settings.points
                settings.player_records.to_csv('data/players.csv', sep=';')
            pygame.quit()
            sys.exit()
        for event in events:
            if event.type == pygame.QUIT:
                if settings.player_records.loc[settings.username, 'record'] < settings.points:
                    settings.player_records.loc[settings.username, 'record'] = settings.points
                    settings.player_records.to_csv('data/players.csv', sep=';')
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return
                
        window.blit(continue_txt, (settings.WIDTH // 2 - continue_txt.get_width() // 2,
                                   settings.HEIGHT // 2 - continue_txt.get_height() // 2))
        window.blit(score_txt, (settings.WIDTH // 2 - score_txt.get_width() // 2,
                                settings.HEIGHT // 2 + continue_txt.get_height() // 2))
        window.blit(record_txt, (settings.WIDTH // 2 - record_txt.get_width() // 2,
                                 settings.HEIGHT // 2 + continue_txt.get_height() + score_txt.get_height() // 2))
        pygame_widgets.update(events)
        pygame.display.update()
        