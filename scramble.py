import random


MOVES: [str] = ['U', 'D', 'R', 'L', 'F', 'B']
DIRECTIONS: [str] = ['', '\'', '2']
OPPOSITES = {'U': 'UD', 'D': 'UD', 'R': 'RL', 'L': 'RL', 'F': 'FB', 'B': 'FB'}


def generate_scramble(scramble_length: int = 20) -> str:
    scramble = [random.choice(MOVES) + random.choice(DIRECTIONS)]

    for i in range(scramble_length - 1):
        move = random.choice(MOVES)
        while move in OPPOSITES[scramble[i][0]]:
            move = random.choice(MOVES)
        
        scramble.append(move + random.choice(DIRECTIONS))

    return ' '.join(scramble)


def scramble_3x3() -> str:
    return generate_scramble(random.randint(20, 22))


def scramble_2x2():
    return generate_scramble(random.randint(20, 22))