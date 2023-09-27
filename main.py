from os import environ

from sorter import Sorter

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import random

import pygame  # import after disabling prompt

import menu
from consts import *

pygame.font.init()
font = pygame.font.Font(None, 25)


def get_random_array(length):
    array = [i * 2 for i in range(length)]
    random.shuffle(array)
    return array


def main():

    # set up pygame
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    while True:

        algo = menu.menu(win)

        # game loop
        surf = pygame.Surface((WIDTH, int(HEIGHT / 3)))
        surf.fill(WHITE)
        array = get_random_array(64)
        display = Sorter(array, algo, surf)
        while True:

            surf = display.update(surf)
            if not surf:
                break
            surf = pygame.transform.flip(surf, False, True)
            win.blit(surf, (0, HEIGHT // 6))

            # update screen
            pygame.display.flip()
            win.fill(WHITE)
            surf.fill(WHITE)

            # check for input
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
