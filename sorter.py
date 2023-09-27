import pygame

from consts import *


class Sorter:
    def __init__(self, array, algo, screen):
        self.array = list(array)
        self.instructions = algo(array)
        self.x_scale = (screen.get_width() - 40) // len(array)
        self.y_scale = (screen.get_height() - 60) / max(array)
        self.y_offset = 60
        self.x_offset = 20
        self.pointers = {}

        self.end_index = 0

    def draw(self, screen):
        # draw array
        for index, i in enumerate(self.array):
            x = self.x_offset + self.x_scale * index
            y = self.y_offset
            pygame.draw.rect(
                screen, BLACK, (x, y, self.x_scale, i * self.y_scale), border_radius=3
            )
        for row, pointer in enumerate(self.pointers.items()):
            _, (colour, index) = pointer
            x = self.x_offset + self.x_scale * index
            y = self.y_offset - 2 - ((row + 1) * 15)
            pygame.draw.rect(screen, colour, (x, y, self.x_scale, 15), border_radius=3)

    def end(self, screen):
        if self.end_index > len(self.array):
            return False
        self.end_index += 1
        for index, i in enumerate(self.array):
            if index <= self.end_index:
                colour = LIME
            else:
                colour = BLACK

            x = self.x_offset + self.x_scale * index
            y = self.y_offset
            pygame.draw.rect(
                screen, colour, (x, y, self.x_scale, i * self.y_scale), border_radius=3
            )
        return screen

    def update(self, screen):
        """
        instructions [("pointer"|"swap"|"mp", index(s))]
        """
        self.draw(screen)
        try:
            cur_instruction = next(self.instructions)
        except StopIteration:
            return self.end(screen)
        if cur_instruction[0] == "pointer":
            # print(f"Add pointer {cur_instruction[1]['id']}")
            self.pointers[cur_instruction[1]["id"]] = (
                cur_instruction[1]["colour"],
                cur_instruction[1]["index"],
            )

        if cur_instruction[0] == "mp":
            # print(
            # f"move pointer {cur_instruction[1][0]} from {self.pointers[cur_instruction[1][0]][1]} to {cur_instruction[1][1]}"
            # )
            # update pointer pos
            self.pointers[cur_instruction[1][0]] = (
                self.pointers[cur_instruction[1][0]][0],
                cur_instruction[1][1],
            )

        if cur_instruction[0] == "swap":
            index1, index2 = cur_instruction[1]

            i1, i2 = self.array[index1], self.array[index2]
            # print("swap", index1, index2)
            for i, index in zip((i1, i2), (index1, index2)):
                pygame.draw.rect(
                    screen,
                    YELLOW,
                    (
                        (self.x_offset + self.x_scale * index),
                        self.y_offset,
                        self.x_scale,
                        i * self.y_scale,
                    ),
                    border_radius=3,
                )
            self.array[index1], self.array[index2] = (
                self.array[index2],
                self.array[index1],
            )
        return screen
