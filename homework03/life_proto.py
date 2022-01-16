import random as rn
import typing as tp
from pprint import pprint as pp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10
    ) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        self.speed = speed
        self.grid = self.create_grid(True)

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw_lines()
            self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
            self.grid = self.get_next_gen()
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        if randomize:
            return [
                [rn.randint(0, 1) for _ in range(self.cell_width)] for _ in range(self.cell_height)
            ]
        return [[0 for _ in range(self.cell_width)]] * self.cell_height

    def draw_grid(self) -> None:
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                coord = (
                    j * self.cell_size + 1,
                    i * self.cell_size + 1,
                    self.cell_size - 1,
                    self.cell_size - 1,
                )
                if self.grid[i][j] == 1:
                    pygame.draw.rect(self.screen, pygame.Color("green"), coord)
                else:
                    pygame.draw.rect(self.screen, pygame.Color("white"), coord)

    def get_neighbours(self, cell: Cell) -> Cells:
        neighbours = []
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                if i == -1:
                    i = self.cell_height - 1
                if i == self.cell_height:
                    i = 0
                if j == -1:
                    j = self.cell_width - 1
                if j == self.cell_width:
                    j = 0
                if (i, j) != cell:
                    neighbours.append(self.grid[i][j])
        return neighbours

    def get_next_gen(self) -> Grid:
        next_grid = self.grid
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                status = self.grid[i][j]
                alive = 0
                for cell in self.get_neighbours((i, j)):
                    if cell == 1:
                        alive += 1
                if status == 1 and alive in (1, 4, 5, 6, 7, 8):
                    next_grid[i][j] = 0
                elif status == 0 and alive == 3:
                    next_grid[i][j] = 1
        return next_grid


if __name__ == "__main__":
    game = GameOfLife(320, 240, 20)
    pp(game.grid)
    game.run()
