import pathlib
import random as rn
import typing as tp
from copy import deepcopy

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
        max_generations=float("inf"),
    ) -> None:
        self.rows, self.cols = size
        self.prev_generation = self.create_grid()
        self.curr_generation = self.create_grid(randomize=randomize)
        self.max_generations = max_generations
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        if randomize:
            return [[rn.randint(0, 1) for _ in range(self.cols)] for _ in range(self.rows)]
        return [[0 for _ in range(self.cols)]] * self.rows

    def get_neighbours(self, cell: Cell) -> Cells:
        neighbours = []
        rows = len(self.curr_generation)
        cols = len(self.curr_generation[1]) if rows else 0
        for row in range(max(0, cell[0] - 1), min(rows, cell[0] + 2)):
            for col in range(max(0, cell[1] - 1), min(cols, cell[1] + 2)):
                if (row, col) != cell:
                    neighbours.append(self.curr_generation[row][col])
        return neighbours

    def get_next_generation(self) -> Grid:
        next_grid = deepcopy(self.curr_generation)
        for i in range(self.rows):
            for j in range(self.cols):
                status = self.curr_generation[i][j]
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
            self.prev_generation, self.curr_generation = (
                self.curr_generation,
                self.get_next_generation(),
            )
            self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.generations > self.max_generations:
            return True
        return False

    @property
    def is_changing(self) -> bool:
        if self.curr_generation != self.prev_generation:
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
                    file.write(str(self.curr_generation[row][col]))
                file.write("\n")
