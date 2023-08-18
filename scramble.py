import random


MOVES = ['U', 'D', 'R', 'L', 'F', 'B']
DIRECTIONS = ['', '\'', '2']
OPPOSITES = {'U': 'UD', 'D': 'UD', 'R': 'RL', 'L': 'RL', 'F': 'FB', 'B': 'FB'}

SCRAMBLE_LENGTH = 20


def generate_scramble() -> str:
    scramble = [random.choice(MOVES) + random.choice(DIRECTIONS)]

    for i in range(SCRAMBLE_LENGTH - 1):
        move = random.choice(MOVES)
        while move in OPPOSITES[scramble[i][0]]:
            move = random.choice(MOVES)
        
        scramble.append(move + random.choice(DIRECTIONS))

    return ' '.join(scramble)


print(generate_scramble())