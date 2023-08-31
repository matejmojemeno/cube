import numpy as np


class ScrambleVisual:
    WHITE: int = 0
    ORANGE: int = 1
    GREEN: int = 2
    RED: int = 3
    BLUE: int = 4
    YELLOW: int = 5

    def __init__(self):
        self.side_colors: list[np.ndarray] = [np.ones((3, 3)) * i for i in range(6)]

    def right_turn(self):
        self.side_colors[self.RED] = np.rot90(self.side_colors[self.RED], axes=(1, 0))
        green_side_copy = self.side_colors[self.GREEN][:, 2].copy()
        self.side_colors[self.GREEN][:, 2] = self.side_colors[self.YELLOW][:, 2]
        self.side_colors[self.YELLOW][:, 2] = self.side_colors[self.BLUE][:, 0]
        self.side_colors[self.BLUE][:, 0] = self.side_colors[self.WHITE][:, 2]
        self.side_colors[self.WHITE][:, 2] = green_side_copy

    def left_turn(self):
        self.side_colors[self.ORANGE] = np.rot90(self.side_colors[self.ORANGE])
        green_side_copy = self.side_colors[self.GREEN][:, 0].copy()
        self.side_colors[self.GREEN][:, 0] = self.side_colors[self.WHITE][:, 0]
        self.side_colors[self.WHITE][:, 0] = self.side_colors[self.BLUE][:, 2]
        self.side_colors[self.BLUE][:, 2] = self.side_colors[self.YELLOW][:, 0]
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
        self.side_colors[self.YELLOW] = np.rot90(self.side_colors[self.YELLOW])
        green_side_copy = self.side_colors[self.GREEN][2, :].copy()
        self.side_colors[self.GREEN][2, :] = self.side_colors[self.RED][2, :]
        self.side_colors[self.RED][2, :] = self.side_colors[self.BLUE][2, :]
        self.side_colors[self.BLUE][2, :] = self.side_colors[self.ORANGE][2, :]
        self.side_colors[self.ORANGE][2, :] = green_side_copy
