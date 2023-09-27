import pygame
from consts import *

pygame.font.init()


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, text):

        super().__init__()
        self.image = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.clicked = False
        self.update_image()

    def update_image(self):

        self.image.fill(WHITE)
        # draw the boreder
        outer_rect = (0, 0, BUTTON_WIDTH, BUTTON_HEIGHT)
        inner_rect = (3, 3, BUTTON_WIDTH - 6, BUTTON_HEIGHT - 6)
        pygame.draw.rect(self.image, BLACK, outer_rect, border_radius=2)
        pygame.draw.rect(self.image, WHITE, inner_rect, border_radius=5)

        # draw the text
        text_surface = self.font.render(self.text, True, BLACK)
        # text_surface.fill((254, 240, 0))
        x = (BUTTON_WIDTH - text_surface.get_width()) // 2
        y = (BUTTON_HEIGHT - text_surface.get_height()) // 2

        # y += text_surface.get_height() // 2
        self.image.blit(text_surface, (x, y))

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)

    def update(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
