import pygame.time
import settings


def delta_time():
    return pygame.time.Clock().tick(settings.FPS) / 1000
