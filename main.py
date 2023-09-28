from copy import deepcopy
from os import environ
import sys

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import numpy as np
import pygame

import menu
import algos
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
        else:
            run_all(win, clock)


def run_singlton(win, clock, algo, name):
    # setup -------------------------------------------->
    surf = pygame.Surface((WIDTH * 0.875, HEIGHT * 0.875))
    surf.fill(WHITE)

    array = get_random_array(ALGO_DATA[name]["size"])
    sort_display = Sorter(array, algo, surf)

    while True:

        surf = sort_display.update(surf)
        if not surf:
            break
        surf = pygame.transform.flip(surf, False, True)
        win.blit(surf, (WIDTH // 16, HEIGHT // 8))

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


def run_all(win, clock):
    # setup -------------------------------------------->

    array = get_random_array(64)
    algos_list = [
        algos.bubble_sort,
        algos.selection_sort,
        algos.insertion_sort,
        algos.merge_sort,
        algos.quick_sort,
    ]
    algo_text = {
        algos.bubble_sort: "Bubble sort",
        algos.selection_sort: "Selection sort",
        algos.insertion_sort: "Insertion sort",
        algos.merge_sort: "Merge sort",
        algos.quick_sort: "Quick sort",
    }
    working_width = WIDTH * 0.875
    working_height = HEIGHT * 0.875
    base_surf = pygame.Surface((working_width / 2 - 15, working_height / 3 - 15))
    base_surf.fill(WHITE)
    font = pygame.font.Font(None, 46)

    sort_displays = [Sorter(deepcopy(array), algo, base_surf) for algo in algos_list]
    surfs = []
    for i in algos_list:
        surf = base_surf.copy()
        surfs.append(surf)

    colours = [BLUE, RED, GREEN, YELLOW, GRAY]

    while True:
        done_count = 0
        for index, i in enumerate(sort_displays):

            grid_x = 0 if index % 2 == 0 else 1
            grid_y = index // 2
            surf = base_surf.copy()
            surf = i.update(surf)
            if not surf:
                surf = surfs[index]
                done_count += 1
            else:
                surfs[index] = surf
            # surf.fill(colours[index])
            if not surf:
                break

            x = (WIDTH // 16) + (working_width / 2) * grid_x
            y = (HEIGHT // 8) + (working_height / 3 + 5) * (grid_y)

            surf = pygame.transform.flip(surf, False, True)
            text = font.render(algo_text[i.algo], True, BLACK)

            win.blit(text, (x, y - text.get_height()))
            win.blit(surf, (x, y))

        if done_count == 5:
            return

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
