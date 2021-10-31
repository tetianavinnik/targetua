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



def get_words(file1, letters):
    with open(file1, 'r') as file:
        word_lst = []
        for line in file:
            line = line + ' '
            line = line.strip().split()
            word = line[0]
            word = word.encode('cp1251', 'ignore').decode( 'utf-8', 'ignore')
            if word != '':
                line[0] = word
                line = ' '.join(line)
                if word[0] in letters and len(word) <= 5 :
                    # line = line[:line.index(' ')]
                    if '/adj' in line:
                        part = 'adjective'
                        line = [word, part]
                    elif 'n' in line or 'noun' in line and 'noninfl' not in line and 'intj' not in line:
                        part = 'noun'
                        line = [word, part]
                    elif '/v' in line:
                        part = 'verb'
                        line = [word, part]
                    elif 'adv' in line:
                        part = 'adverb'
                        line = [word, part]
                    word_lst.append(line)
        print(word_lst)


get_words("base.txt", generate_grid())
