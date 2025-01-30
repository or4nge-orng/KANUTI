import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
import sys
from pandas import read_csv

from settings import WIDTH, HEIGHT


player_records = read_csv('data/players.csv', delimiter=';', index_col='id')
    

username = ''


def set_username_check():
    global username
    username = name_input.getText()


def check_username(username):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN] and username in list(player_records['username']) and username:
        return True
    elif keys[pygame.K_RETURN] and username not in list(player_records['username']) and username:
        player_records.loc[len(player_records) + 1] = [username, 0]
        player_records.to_csv('data/players.csv', sep=';')
        return False



def start_menu(window):
    btn_size = 200, 50
    menu_font = pygame.font.SysFont('arial', 30, bold=True)
    start_btn = Button(window, WIDTH * 0.08, HEIGHT * 0.77 - 80,
                                            *btn_size, text='Start',
                                            inactiveColour=(220, 220, 220), hoverColour=(180, 180, 180),
                                            radius=btn_size[0] // 10, font=menu_font)

    exit_btn = Button(window, WIDTH * 0.08, HEIGHT * 0.77,
                                            *btn_size, text='Exit',
                                            inactiveColour=(220, 220, 220), hoverColour=(180, 180, 180), 
                                            radius=btn_size[0] // 10, font=menu_font)
    while True:
        window.fill('black')
        events = pygame.event.get()
        if start_btn.clicked:
            global name_input
            name_input = TextBox(window, WIDTH // 2 - 200, HEIGHT // 2, 400, 50, fontSize=30, onSubmit=set_username_check)
            
        if check_username(username):
            return
        else:
            print('false')
        
            
        if exit_btn.clicked:
            pygame.quit()
            sys.exit()
            
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()                                         
            
        pygame_widgets.update(events)
        pygame.display.update()