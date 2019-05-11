
def carrecta_list(list, count):
    list_one = list.split()

    correct = [int(x) for x in list_one if int(x) <= 100000]
    # 1<= N <=1000
    if len(correct) > 0 and len(correct) == count:
        return True, correct

    return False, correct


def neighbours_new_year_party(lista, count):

    suma1 = 0
    elemento1 = ''
    suma2 = 0
    elemento_2 = ''
    lista = lista[::-1]


    for key, elemento in enumerate(lista):
        if (key + 2) >= count:
            break

        if suma1 == 0:
            suma1 = int(elemento) + int(lista[key + 2])
            if elemento <= 0:
                elemento1 = str(lista[key + 2])
            elif lista[key + 2] <= 0:
                elemento1 = str(elemento)
            else:
                elemento1 = str(elemento) + str(lista[key + 2])
        elif suma2 == 0 or suma2 > suma1:
            suma2 = int(elemento) + int(lista[key + 2])
            if elemento <= 0:
                elemento_2 = str(lista[key + 2])
            elif lista[key + 2] <= 0:
                elemento_2 = str(elemento)
            else:
                elemento_2 = str(elemento) + str(lista[key + 2])

    if suma1 > suma2:
        print(elemento1)
    elif suma1 == suma2 and min(lista) < 0:
        print(max(lista))
    else:
        print(elemento_2)



def main():

    correct_tickets = False
    testcase = int(input())


    for x in range(testcase):
        try:


            #1 <= T <= 10
            if testcase <= 0 or testcase > 11:
                print('Test case must be between 1 and 10')

            ticket = int(input())

            #1 <= N <= 1000
            if ticket <= 0 or ticket >1001:
                print('Test case must be between 1 and 1000')

            while not correct_tickets:
                tickets = input()
                correct_tickets, tickets = carrecta_list(tickets, ticket)

                if not correct_tickets:
                    print('strengths of Villains is not correct')

            neighbours_new_year_party(tickets, ticket)
            correct_tickets = False
        except ValueError:
            print('You must enter only numbers')


main()