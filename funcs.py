import pygame.time
import settings
import player


player = player.Player()
def delta_time():
    return pygame.time.Clock().tick(settings.FPS) / 1000


def check_player_finished() -> bool:
        return (int(player.x) in range(settings.level.nextX * settings.BLOCKSIZE,
                                       settings.level.nextX * settings.BLOCKSIZE + settings.BLOCKSIZE)) and \
              (int(player.y) in range(settings.level.nextY * settings.BLOCKSIZE,
                                      settings.level.nextY * settings.BLOCKSIZE + settings.BLOCKSIZE))
              

def start_timer(window):
    start_time = pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
    pygame.draw
    