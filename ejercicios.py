import math


def anagrama(word, word2):

    word = sorted(word)
    word2 = sorted(word2[::-1])

    if word == word2:
        return True
    else:
        return False


print(print(anagrama('fresa', 'frase')))


def es_polidromo(word):
    polidromo = word[::-1]

    if word == polidromo:
        return True
    else:
        return False


print(es_polidromo('ana'))

print(es_polidromo('arenera'))

print(es_polidromo('mama'))


def factorial(number):
    fac = 1

    for element in range(1, number + 1):
        fac *= element
    return fac

print(math.factorial(5))

print(factorial(5))

