
def carrecta_list(list, count):
    list_one = list.split()

    correct = [int(x) for x in list_one if int(x) <= 100000]
    # 1<= N <=1000
    if len(correct) > 0 and len(correct) == count:
        return True, correct

    return False, correct


def win_lose(strengths_villains, energy_players):

    strengths_villains = sorted(strengths_villains)

    energy_players = sorted(energy_players)
    for key, element in enumerate(strengths_villains):
        if energy_players[key] < element:
            print('LOSE')
            return False

    print('WIN')

def main():
    correct_villains = False
    correct_players = False

    testcase = 1


    for x in range(testcase):
        try:
            testcase = int(input())

            #1 <= T <= 10
            if testcase <= 0 or testcase > 11:
                print('Test case must be between 1 and 10')

            villains_player = int(input())

            #1 <= N <= 1000
            if villains_player <= 0 or villains_player >1001:
                print('Test case must be between 1 and 1000')

            while not correct_villains:
                strengths_villains = input()
                correct_villains, strengths_villains = carrecta_list(strengths_villains, villains_player)

                if not correct_villains:
                    print('strengths of Villains is not correct')



            while not correct_players:
                energy_players = input()
                correct_players, energy_players = carrecta_list(energy_players, villains_player)

                if not correct_players:
                    print('strengths of Villains is not correct')

            win_lose(strengths_villains, energy_players)

        except ValueError:
            print('You must enter only numbers')

main()


'''

Maxi está jugando el juego y en un momento determinado quiere saber si es posible que gane el juego o no con el conjunto dado de energías y fortalezas de los jugadores y villanos. Maxi gana el juego si sus jugadores pueden matar a todos los villanos con la energía asignada.



Formato de entrada
La primera línea de entrada consiste en el número de casos de prueba, T.

La primera línea de cada caso de prueba consiste en el número de villanos y jugadores, N.

La segunda línea de cada caso de prueba consiste en N puntos separados de las fortalezas de los villanos.

La tercera línea de cada caso de prueba consiste en N espacio separado de la energía de los jugadores.



Restricciones
1 <= T <= 10

1 <= N <= 1000

1 <= fuerza, energía <= 100000



Formato de salida
Para cada caso de prueba, imprima WIN si todos los villanos pueden ser asesinados; de lo contrario, imprima LOSE en líneas separadas.

Caso de prueba de muestra 1
Entrada
1 
6 
112 243 512 343 90 478 
500 789 234 400 452 150
Salida
GANAR
Explicación
Para el caso de prueba dado, si barajamos a los jugadores y villanos, podemos observar que todos los villanos pueden ser asesinados por los jugadores.




Como todos los villanos pueden ser asesinados por los jugadores, MAXI GANARÁ el juego. Por lo tanto, la salida final es WIN.
Caso de prueba de muestra 2
Entrada
2 
6 
10 20 50 100 500 400 
30 20 60 70 90 490 
5 
10 20 30 40 50 
40 50 60 70 80
Salida
PERDER
GANAR

'''