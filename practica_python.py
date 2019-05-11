
import operator
import random
from collections import defaultdict
import os

'''
all_words = "all the words in the world".split()

def get_random_word():

    return random.choice(all_words)



def unique_word():
    words = []

    for _ in range(1000):
        word = get_random_word()

        if word not in words:
            words.append(word)

    return words


def unique_word2():
    words = set()

    for _ in range(1000):
        words.add(get_random_word())
    return words

print(unique_word())
print()
print(unique_word2())


cowboy = {'age': 32, 'horse': 'mustang', 'hat_size': 'large'}

nombre = cowboy.get('age', 'the man with not name')



print(nombre)
print(cowboy)



grades = [
    ('elliot', 91),
    ('neelam', 98),
    ('bianca', 81),
    ('elliot', 88),
]

student_grades = defaultdict(list)

for name, grade in grades:
    student_grades[name] = grade

print(student_grades)


home = str(os.path.expanduser('~octavio'))
print(home)
'''
data = (
('betty', 1),
('bought', 1),
('a', 1),
('bit', 1),
('of', 1),
('butter', 2),
('but', 1),
('the', 1),
('was', 1),
('bitter', 1))

sorted_x = sorted(data, key=operator.itemgetter(1))

print(sorted_x)

home = str(os.path.expanduser('~octavio'))
print(home)


