import pygame


class Square:

    def __init__(self, v: int):
        self.value: int = v

    def get_color(self):
        color_switcher = {
            0: (192, 192, 192),     # Dark gray (Unoccupied)
            2: (250, 250, 250),     # white
            4: (204, 255, 153),     # Green
            8: (255, 153, 51),      # Orange
            16: (204, 102, 102),    # Dark orange - light red
            32: (255, 51, 51),      # Light Red
            64: (255, 0, 0),        # Red
            128: (255, 255, 153),   # Pale yellow
            256: (255, 255, 102),   # Less pale yellow
            512: (255, 255, 51),    # Even less pale yellow
            1024: (255, 255, 0),  # Yellow
            2048: (204, 204, 0),    # Gold
        }
        return color_switcher[self.value]

    def show(self, display, size, padding, x, y):
        pygame.draw.rect(display, self.get_color(), ((padding + size) * x + padding,
                                                     (padding + size) * y + padding,
                                                     size,
                                                     size))
        if self.value > 0:
            display.blit(pygame.font.SysFont('arial', size - 35).render(str(self.value), False, (0, 0, 0)),
                         ((padding + size) * x + padding + (size - 10) * (5 - len(str(self.value))) * 0.1, (padding + size) * y + padding + size * 0.15))
