from PyQt6.QtGui import QColor, QPainter, QBrush, QPen
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene
import numpy as np

from termcolor import colored


class ScrambleVisual:
    WHITE: int = 0
    ORANGE: int = 1
    GREEN: int = 2
    RED: int = 3
    BLUE: int = 4
    YELLOW: int = 5

    MOVES_COUNT = {"": 1, "2": 2, "'": 3}
    COLORS = {
        WHITE: QColor(255, 255, 255),
        ORANGE: QColor(255, 165, 0),
        GREEN: QColor(0, 255, 0),
        RED: QColor(255, 0, 0),
        BLUE: QColor(0, 0, 255),
        YELLOW: QColor(255, 255, 0),
    }

    T_COLORS = {
        WHITE: 'white',
        ORANGE: 'light_red',
        GREEN: 'green',
        RED: 'red',
        BLUE: 'blue',
        YELLOW: 'light_yellow'
    }

    def __init__(self):
        self.side_colors: list[np.ndarray] = [np.ones((3, 3)) * i for i in range(6)]

        self.moves = {
            "R": self.right_turn,
            "L": self.left_turn,
            "U": self.up_turn,
            "D": self.down_turn,
            "F": self.front_turn,
            "B": self.back_turn,
        }

    def right_turn(self):
        self.side_colors[self.RED] = np.rot90(self.side_colors[self.RED], axes=(1, 0))
        green_side_copy = self.side_colors[self.GREEN][:, 2].copy()
        self.side_colors[self.GREEN][:, 2] = self.side_colors[self.YELLOW][:, 2]
        self.side_colors[self.YELLOW][:, 2] = self.side_colors[self.BLUE][:, 0][::-1]
        self.side_colors[self.BLUE][:, 0] = self.side_colors[self.WHITE][:, 2][::-1]
        self.side_colors[self.WHITE][:, 2] = green_side_copy

    def left_turn(self):
        self.side_colors[self.ORANGE] = np.rot90(
            self.side_colors[self.ORANGE], axes=(1, 0)
        )
        green_side_copy = self.side_colors[self.GREEN][:, 0].copy()
        self.side_colors[self.GREEN][:, 0] = self.side_colors[self.WHITE][:, 0]
        self.side_colors[self.WHITE][:, 0] = self.side_colors[self.BLUE][:, 2][::-1]
        self.side_colors[self.BLUE][:, 2] = self.side_colors[self.YELLOW][:, 0][::-1]
        self.side_colors[self.YELLOW][:, 0] = green_side_copy

    def up_turn(self):
        self.side_colors[self.WHITE] = np.rot90(
            self.side_colors[self.WHITE], axes=(1, 0)
        )
        green_side_copy = self.side_colors[self.GREEN][0, :].copy()
        self.side_colors[self.GREEN][0, :] = self.side_colors[self.RED][0, :]
        self.side_colors[self.RED][0, :] = self.side_colors[self.BLUE][0, :]
        self.side_colors[self.BLUE][0, :] = self.side_colors[self.ORANGE][0, :]
        self.side_colors[self.ORANGE][0, :] = green_side_copy

    def down_turn(self):
        self.side_colors[self.YELLOW] = np.rot90(
            self.side_colors[self.YELLOW], axes=(1, 0)
        )
        green_side_copy = self.side_colors[self.GREEN][2, :].copy()
        self.side_colors[self.GREEN][2, :] = self.side_colors[self.ORANGE][2, :]
        self.side_colors[self.ORANGE][2, :] = self.side_colors[self.BLUE][2, :]
        self.side_colors[self.BLUE][2, :] = self.side_colors[self.RED][2, :]
        self.side_colors[self.RED][2, :] = green_side_copy

    def front_turn(self):
        self.side_colors[self.GREEN] = np.rot90(
            self.side_colors[self.GREEN], axes=(1, 0)
        )
        white_side_copy = self.side_colors[self.WHITE][2, :].copy()
        self.side_colors[self.WHITE][2, :] = self.side_colors[self.ORANGE][:, 2][::-1]
        self.side_colors[self.ORANGE][:, 2] = self.side_colors[self.YELLOW][0, :]
        self.side_colors[self.YELLOW][0, :] = self.side_colors[self.RED][:, 0][::-1]
        self.side_colors[self.RED][:, 0] = white_side_copy

    def back_turn(self):
        self.side_colors[self.BLUE] = np.rot90(
            (self.side_colors[self.BLUE]), axes=(1, 0)
        )
        white_side_copy = self.side_colors[self.WHITE][0, :].copy()
        self.side_colors[self.WHITE][0, :] = self.side_colors[self.RED][:, 2]
        self.side_colors[self.RED][:, 2] = self.side_colors[self.YELLOW][2, :][::-1]
        self.side_colors[self.YELLOW][2, :] = self.side_colors[self.ORANGE][:, 0]
        self.side_colors[self.ORANGE][:, 0] = white_side_copy[::-1]

    def apply_scramble(self, scramble: list[str]):
        for move in scramble:
            for _ in range(self.MOVES_COUNT[move[1:]]):
                self.moves[move[0]]()
            # print(move)
            # self.print_cube()

        return self.side_colors
    
    def print_cube(self):
        for side in self.side_colors:
            for i in range(3):
                for j in range(3):
                    print(colored('W', self.T_COLORS[side[i, j]]), end = '')
                print()
            print()
        print("=====================")

# scramble = "L U' B R F2 L U2 B' D2 F R2 D L D2 L F R' F2 U L'".split()
# ScrambleVisual().apply_scramble(scramble)