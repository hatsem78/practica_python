'''def area_tringulo(base, altura):
    return (base * altura) / 2 '''


area = lambda base, altura: base*altura/2
print(area(2, 7))


numeros = [17, 24, 7, 39, 8, 51, 92]

def numeros_par(numero):
    if numero % 2 == 0:
        return numero

#utilizando filter retorna una lista reducida por la condicion que se le asigna

print(list(filter(numeros_par, numeros)))

#filter utilizando una funcion lambda

print(list(filter(lambda numero_par: numero_par % 2 == 0, numeros )))



