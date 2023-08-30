import numpy as np

WHITE = 0
ORANGE = 1
GREEN = 2
RED = 3
BLUE = 4
YELLOW = 5

side_colors = [np.ones((3,3)) * i for i in range(6)]

def right_turn():
    np.rot90(side_colors[RED])
    green_side_copy = side_colors[GREEN][:,2].copy()
    side_colors[GREEN][:,2] = side_colors[YELLOW][:,2]
    side_colors[YELLOW][:,2] = side_colors[BLUE][:,0]
    side_colors[BLUE][:,0] = side_colors[WHITE][:,2]
    side_colors[WHITE][:,2] = green_side_copy


def right_prime_turn():
    for i in range(3):
        right_turn()


def left_turn():
    np.rot90(side_colors[ORANGE])
    green_side_copy = side_colors[GREEN][:,0].copy()
    side_colors[GREEN][:,0] = side_colors[WHITE][:,0]
    side_colors[WHITE][:,0] = side_colors[BLUE][:,2]
    side_colors[BLUE][:,2] = side_colors[YELLOW][:,0]
    side_colors[YELLOW][:,0] = green_side_copy


def left_prime_turn():
    for i in range(3):
        left_turn()

left_turn()
for i in range(6):
    print(side_colors[i])
    print()