import pygame
import math
import settings


def raycast(window, player):
    BS = settings.BLOCKSIZE
    inBlockPos = {'left': player.x - player.x // BS * BS,
                      'right': BS - (player.x - player.x // BS * BS),
                      'top': player.y - player.y // BS * BS,
                      'bottom': BS - (player.y - player.y // BS * BS)}
    for ray in range(settings.RAY_NUM):
        ray_angle = player.angle - settings.HALF_FOV + settings.dr * ray
        cos_a, sin_a = math.cos(ray_angle), math.sin(ray_angle)
        vl, hl = 0, 0
        for k in range(settings.MAP_SIZE):
            if cos_a < 0:
                vl = inBlockPos['left'] / -cos_a + BS / -cos_a * k + 1
            elif cos_a > 0:
                vl = inBlockPos['right'] / cos_a + BS / cos_a * k + 1
                
            xw, yw = player.x + vl * cos_a, player.y + vl * sin_a
            block = xw // BS * BS, yw // BS * BS
            if block in settings.block_map:
                break
                
        for k in range(settings.MAP_SIZE):
            if sin_a < 0:
                hl = inBlockPos['top'] / -sin_a + BS / -sin_a * k + 1
            elif sin_a > 0:
                hl = inBlockPos['bottom'] / sin_a + BS / sin_a * k + 1
                
            xh, yh = player.x + hl * cos_a, player.y + hl * sin_a
            block = xh // BS * BS, yh // BS * BS
            if block in settings.block_map:
                break

        ray_size = min(vl, hl) / BS
        
        toX, toY = ray_size * BS * math.cos(ray_angle) + player.x, \
            ray_size * BS * math.sin(ray_angle) + player.y
        #pygame.draw.line(window, 'red', (player.x, player.y), (toX, toY), 1)
        ray_size *= math.cos(ray_angle - player.angle - 0.0001)
        line_height = settings.HEIGHT // ray_size
        half_height = settings.HEIGHT // 2
        draw_start = -line_height / 2 + half_height
        if draw_start < 0:
            draw_start = 0
        draw_end = line_height / 2 + half_height
        if draw_end >= settings.HEIGHT:
            draw_end = settings.HEIGHT - 1
        #print((vl, hl), (settings.level.nextX, settings.level.nextY))
        #print(int(player.x), int(player.y), int(toX), int(toY))
        c = 255 / (1 + line_height ** 2 * 0.000002)
        scale = settings.WIDTH // settings.RAY_NUM
        if settings.finish.clipline((player.x, player.y), (toX, toY)):
            pygame.draw.line(window, (255 - c % 255, 0, 0),
                            (scale * ray, draw_end), (scale * ray, draw_start), scale)
        else:
            pygame.draw.line(window, (255 - c % 255, 255 - c % 255, 255 - c % 255),
                            (scale * ray, draw_end), (scale * ray, draw_start), scale)

        