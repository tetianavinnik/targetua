from typing import List
import string
import random
import operator
import copy

def generate_grid() -> List[List[str]]:
    alphabet = [i for i in range(1072, 1098)] +[1169] + [i for i in range(1100, 1073)]
    playground = []
    while len(playground) != 5:
        letter = random.choice(alphabet)
        letter = chr(letter)
        if letter not in playground:
            playground.append(letter)
    return playground
print(generate_grid())