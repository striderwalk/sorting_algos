import pygame
from pygame.locals import *

import algos
import button
from consts import *


def menu(screen, clock):

    algos_dict = {
        "Bubble sort": algos.bubble_sort,
        "Selection sort": algos.selection_sort,
        "Insertion sort": algos.insertion_sort,
        "Merge sort": algos.merge_sort,
        "Quick sort": algos.quick_sort,
    }

    button_group = pygame.sprite.Group()
    start_x = (WIDTH - BUTTON_WIDTH) // 2
    start_y = (HEIGHT - len(algos_dict) * 45) // 2

    button_group.add(
        button.Button(start_x, start_y + 45 * index, text)
        for index, text in enumerate(algos_dict)
    )

    font = pygame.font.Font(None, 46)
    text = font.render("Pick your sort!", True, BLACK)
    text_x = (WIDTH - text.get_width()) // 2
    text_y = 40
    running = True

    while running:
        screen.blit(text, (text_x, text_y))
        button_group.draw(screen)

        button_group.draw(screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                for i in button_group:
                    if i.update():
                        if i.text != "All":
                            return {"text": i.text, "algo": algos_dict[i.text]}

        pygame.display.flip()
        clock.tick(FPS)
        screen.fill((255, 255, 255))

    pygame.quit()
