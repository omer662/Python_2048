import pygame
from Board import Board
import random


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Omer's 2048")
        self.board = Board()
        self.last = []
        self.board.show()

    def handle_events(self) -> bool:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.board.up()
                    if self.board.grid != self.last:
                        self.add_random_block()
                elif event.key == pygame.K_LEFT:
                    self.board.left()
                    if self.board.grid != self.last:
                        self.add_random_block()
                elif event.key == pygame.K_DOWN:
                    self.board.down()
                    if self.board.grid != self.last:
                        self.add_random_block()
                elif event.key == pygame.K_RIGHT:
                    print(self.last)
                    self.board.right()
                    print(self.last)
                    if self.board.grid != self.last:
                        self.add_random_block()
            if event.type == pygame.QUIT:
                return True
        return False

    def add_random_block(self):
        value = 2 ** (int(random.randint(1, 10) > 7) + 1)
        opts = [(row, col) for col in range(self.board.grid_size) for row in range(self.board.grid_size)
                if self.board.grid[row][col] is None]
        if len(opts) == 0:
            return True
        position = opts[random.randint(0, len(opts) - 1)]
        self.board.add(value, position)
        return False

    def run(self):
        stop = False
        # Add initial 2 blocks
        self.add_random_block()
        self.add_random_block()
        self.board.show()
        while not stop:
            if self.handle_events():
                break
            self.board.show()
            self.last = self.board.grid.copy()
