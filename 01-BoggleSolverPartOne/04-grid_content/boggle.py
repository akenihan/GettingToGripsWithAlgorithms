from string import ascii_uppercase
from random import choice


def make_grid(width, height):
    return {(row, col): choice(ascii_uppercase)
        for row in range(height)
        for col in range(width)}
