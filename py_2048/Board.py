import pygame
from Square import Square


class Board:

    def __init__(self):
        self.grid_size = 5
        self.square_size = 75
        self.padding = 5
        self.display = pygame.display.set_mode(((self.square_size + self.padding) * self.grid_size + self.padding,
                                                (self.square_size + self.padding) * self.grid_size + self.padding))
        self.bg_color = (128, 128, 128)
        self.grid = [[None for j in range(self.grid_size)] for i in range(self.grid_size)]

    def up(self):
        for col in range(self.grid_size):
            compare_to = 0
            for row in range(self.grid_size):
                if self.grid[row][col] is not None:
                    if self.grid[compare_to][col] is None:
                        self.grid[compare_to][col] = self.grid[row][col]
                        self.grid[row][col] = None
                    elif compare_to != row:
                        if self.grid[compare_to][col].value == self.grid[row][col].value:
                            self.grid[compare_to][col] = Square(self.grid[compare_to][col].value * 2)
                            self.grid[row][col] = None
                            compare_to += 1
                        else:
                            self.grid[compare_to + 1][col] = self.grid[row][col]
                            if compare_to + 1 != row:
                                self.grid[row][col] = None
                            compare_to += 1

    def left(self):
        for row in range(self.grid_size):
            compare_to = 0
            for col in range(self.grid_size):
                if self.grid[row][col] is not None:
                    if self.grid[row][compare_to] is None:
                        self.grid[row][compare_to] = self.grid[row][col]
                        self.grid[row][col] = None
                    elif compare_to != col:
                        if self.grid[row][compare_to].value == self.grid[row][col].value:
                            self.grid[row][compare_to] = Square(self.grid[row][compare_to].value * 2)
                            self.grid[row][col] = None
                            compare_to += 1
                        else:
                            self.grid[row][compare_to + 1] = self.grid[row][col]
                            if compare_to + 1 != col:
                                self.grid[row][col] = None
                            compare_to += 1

    def down(self):
        for col in range(self.grid_size):
            compare_to = self.grid_size - 1
            for row in range(self.grid_size - 1, -1, -1):
                if self.grid[row][col] is not None:
                    if self.grid[compare_to][col] is None:
                        self.grid[compare_to][col] = self.grid[row][col]
                        self.grid[row][col] = None
                    elif compare_to != row:
                        if self.grid[compare_to][col].value == self.grid[row][col].value:
                            self.grid[compare_to][col] = Square(self.grid[compare_to][col].value * 2)
                            self.grid[row][col] = None
                            compare_to -= 1
                        else:
                            self.grid[compare_to - 1][col] = self.grid[row][col]
                            if compare_to - 1 != row:
                                self.grid[row][col] = None
                            compare_to -= 1

    def right(self):
        for row in range(self.grid_size):
            compare_to = self.grid_size - 1
            for col in range(self.grid_size - 1, -1, -1):
                if self.grid[row][col] is not None:
                    if self.grid[row][compare_to] is None:
                        self.grid[row][compare_to] = self.grid[row][col]
                        self.grid[row][col] = None
                    elif compare_to != col:
                        if self.grid[row][compare_to].value == self.grid[row][col].value:
                            self.grid[row][compare_to] = Square(self.grid[row][compare_to].value * 2)
                            self.grid[row][col] = None
                            compare_to -= 1
                        else:
                            self.grid[row][compare_to - 1] = self.grid[row][col]
                            if compare_to - 1 != col:
                                self.grid[row][col] = None
                            compare_to -= 1

    def show(self):
        self.display.fill(self.bg_color)
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.grid[row][col] is None:
                    Square(0).show(self.display, self.square_size, self.padding, col, row)
                else:
                    self.grid[row][col].show(self.display, self.square_size, self.padding, col, row)
        pygame.display.update()

    def add(self, value, position):
        self.grid[position[0]][position[1]] = Square(value)
