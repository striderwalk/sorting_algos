import pygame

from consts import *

pygame.mixer.init()
BEEP = pygame.mixer.Sound("beep.mp3")


class Sorter:
    def __init__(self, array, algo, screen):
        self.array = list(array)
        self.instructions = algo(array)
        self.algo = algo
        self.x_scale = (screen.get_width()) / len(array)
        self.y_scale = (screen.get_height() - 50) / max(array)
        self.y_offset = 50

        self.pointers = {}

        self.end_index = 0

    def draw(self, screen):
        # screen.fill(GRAY)
        # draw array
        for index, i in enumerate(self.array):
            x = self.x_scale * index
            y = self.y_offset
            pygame.draw.rect(
                screen,
                BLACK,
                (x, y, self.x_scale + 1, i * self.y_scale),
                border_bottom_left_radius=3,
                border_bottom_right_radius=3,
            )
        for row, pointer in enumerate(self.pointers.items()):
            _, (colour, index) = pointer
            x = self.x_scale * index
            y = self.y_offset - 2 - ((row + 1) * 15)
            pygame.draw.rect(screen, colour, (x, y, self.x_scale, 15), border_radius=5)

    def end(self, screen):
        if self.end_index > len(self.array):
            return False
        self.end_index += 1
        for index, i in enumerate(self.array):
            if index <= self.end_index:
                colour = LIME
            else:
                colour = BLACK

            x = self.x_scale * index
            y = self.y_offset
            pygame.draw.rect(
                screen,
                colour,
                (x, y, self.x_scale + 1, i * self.y_scale),
                border_bottom_left_radius=3,
                border_bottom_right_radius=3,
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

            self.pointers[cur_instruction[1]["id"]] = (
                cur_instruction[1]["colour"],
                cur_instruction[1]["index"],
            )

        if cur_instruction[0] == "mp":
            # update pointer pos
            self.pointers[cur_instruction[1][0]] = (
                self.pointers[cur_instruction[1][0]][0],
                cur_instruction[1][1],
            )

        if cur_instruction[0] == "swap":
            # BEEP.play()
            index1, index2 = cur_instruction[1]

            i1, i2 = self.array[index1], self.array[index2]
            for i, index in zip((i1, i2), (index1, index2)):
                x = self.x_scale * index
                y = self.y_offset
                pygame.draw.rect(
                    screen,
                    YELLOW,
                    (x, y, self.x_scale + 1, i * self.y_scale),
                    border_bottom_left_radius=3,
                    border_bottom_right_radius=3,
                )
            self.array[index1], self.array[index2] = (
                self.array[index2],
                self.array[index1],
            )
        return screen
