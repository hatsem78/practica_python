def anagrama(word, word2):
    word2 = sorted(word2[::-1])
    word = sorted(word)

    if word == word2:
        return True
    else:
        return False
print(anagrama('fresa', 'frase'))


def factorial(number):
    aple = 1

    for elemento in range(1,(number+1)):
        aple *= elemento
    return aple
print(factorial(5))