from os import environ
import sys

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import numpy as np
import pygame

import menu
from consts import *
from sorter import Sorter


pygame.font.init()
font = pygame.font.Font(None, 25)


def get_random_array(length):
    return list(np.random.randint(0, 256, size=length))


def main():

    # set up pygame
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    while True:

        algo = menu.menu(win, clock)
        # game loop
        if algo["text"] != "all":
            run_singlton(win, clock, algo["algo"], algo["text"])


def run_singlton(win, clock, algo, name):
    # setup -------------------------------------------->
    surf = pygame.Surface((WIDTH, (HEIGHT / 8) * 7))
    surf.fill(WHITE)

    array = get_random_array(ALGO_DATA[name]["size"])
    sort_display = Sorter(array, algo, surf)

    while True:

        surf = sort_display.update(surf)
        if not surf:
            break
        surf = pygame.transform.flip(surf, False, True)
        win.blit(surf, (0, HEIGHT // 6))

        # check for input
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # reset loop ----------->
        # update the display
        pygame.display.flip()
        win.fill(WHITE)
        surf.fill(WHITE)
        pygame.display.set_caption(f"Sorting demo | {clock.get_fps():.2f}fps")

        # limit fps
        clock.tick(FPS)


if __name__ == "__main__":
    main()
