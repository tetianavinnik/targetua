from typing import List
import random


def generate_grid() -> List[List[str]]:
    """
    Return list of 5 random letters.
    """
    alphabet = [i for i in range(1072, 1098)] +[1169] + [i for i in range(1100, 1073)]
    playground = []
    while len(playground) != 5:
        letter = random.choice(alphabet)
        letter = chr(letter)
        if letter not in playground:
            playground.append(letter)
    return playground


def get_words(file1, letters):
    """
    (str, list) -> list
    Return list of words.
    >>> print(get_words("base.lst", ['щ'])[0])
    ('щасні', 'noun')
    """
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
                if (word[0] in letters and len(word) <= 5 and
                    'noninfl' not in line and 'intj' not in line):
                    if '/n' in line or 'noun' in line:
                        part = "noun"
                        line = (word, part)
                    elif '/v' in line or'verb' in line:
                        part = "verb"
                        line = (word, part)
                    elif 'adj' in line:
                        part = "adjective"
                        line = (word, part)
                    elif 'adv' in line:
                        part = "adverb"
                        line = (word, part)
                    word_lst.append(line)
        return word_lst


def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    (list, str, list, list) -> list
    Return list of right words and missed words.
    """
    right_word = []
    missed_word = []
    for i in user_words:
        if i[0] in letters:
            for name in dict_of_words:
                if i == name[0] and name[0] not in right_word:
                    right_word.append(i)
    for name in dict_of_words:
        if name[0] not in right_word and name[1] == language_part:
            missed_word.append(name[0])
    return right_word, missed_word

print(check_user_words(['бабин', 'битий', 'бичий', 'білий', 'бісів', 'богів', 'божий', 'босий', 'булий', 'булів', 'бурий', 'ласий', 'лисий', 'литий', 'лихий', 'лівий', 'любий', 'лютий', 'усний', 'утлий', 'щирий', 'щучий', 'щучин'], "adjective", ['ф', 'у', 'щ', 'б', 'л'], get_words("base2.lst", ['ф', 'у', 'щ', 'б', 'л'])))