import pygame.time
import settings


def delta_time():
    return pygame.time.Clock().tick(settings.FPS) / 1000


def check_player_finished(player) -> bool:
    return (int(player.x) in range(settings.level.nextX * settings.BLOCKSIZE,
                                    settings.level.nextX * settings.BLOCKSIZE + settings.BLOCKSIZE)) and \
            (int(player.y) in range(settings.level.nextY * settings.BLOCKSIZE,
                                    settings.level.nextY * settings.BLOCKSIZE + settings.BLOCKSIZE))
              
