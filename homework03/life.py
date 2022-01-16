import pathlib
import random as rn
import typing as tp
from copy import deepcopy
from pprint import pprint as pp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_gens: tp.Optional[float] = float("inf"),
    ) -> None:

        self.rows, self.cols = size
        self.prev_gen = self.create_grid()
        self.curr_gen = self.create_grid(True)
        self.max_gens = max_gens
        self.gens = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        if randomize:
            return [[rn.randint(0, 1) for _ in range(self.cols)] for _ in range(self.rows)]
        return [[0 for _ in range(self.cols)]] * self.rows

    def get_neighbours(self, cell: Cell) -> Cells:
        neighbours = []
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                if i == -1:
                    i = self.rows - 1
                if i == self.rows:
                    i = 0
                if j == -1:
                    j = self.cols - 1
                if j == self.cols:
                    j = 0
                if (i, j) != cell:
                    neighbours.append(self.curr_gen[i][j])
        return neighbours

    def get_next_gen(self) -> Grid:
        next_grid = deepcopy(self.curr_gen)
        for i in range(self.rows):
            for j in range(self.cols):
                status = self.curr_gen[i][j]
                alive = 0
                for cell in self.get_neighbours((i, j)):
                    if cell == 1:
                        alive += 1
                if status == 1 and alive in (1, 4, 5, 6, 7, 8):
                    next_grid[i][j] = 0
                elif status == 0 and alive == 3:
                    next_grid[i][j] = 1
        return next_grid

    def step(self) -> None:
        if not self.is_max_generations_exceeded:
            self.prev_gen, self.curr_gen = self.curr_gen, self.get_next_gen()
            self.gens += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.gens > self.max_gens:
            return True
        return False

    @property
    def is_changing(self) -> bool:
        if self.curr_gen != self.prev_gen:
            return True
        return False

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        new_grid = []
        with open(filename, "r") as f:
            for line in f:
                new_grid.append([int(i) for i in line if (i == "0" or i == "1")])
            new_game = GameOfLife((len(new_grid), len(new_grid[0])))
            new_game.curr_generation = new_grid
            return new_game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w") as file:
            for row in range(self.rows):
                for col in range(self.cols):
                    file.write(str(self.curr_gen[row][col]))
                file.write("\n")
