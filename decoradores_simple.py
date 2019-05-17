#los decoradores son funciones que agrega funcionaledades a otras funciones
"""
    la extructura del decorador es
    .tres funciones (A, B, C) donde A recibe como parametro B y devuelve otra función C
    .un decorador devuelve una función
    ejemplo

    def funcion_decorador(funcion):
        def funcion_interna_A():
            #codigo de la función

        return funcion interna funcion_interna_A / paso C

"""

def funcion_decoradora(funcion_parametro):

    def funcion_interna():
        #acciones adicionales
        print("vamos a realizar un cálculo")

        funcion_parametro()
        #se agregan más funcionaledades
        print('hemos terminado el cálculo')
    return funcion_interna


@funcion_decoradora
def suma():
    print(10+5)


def restas():
    print(10-4)


suma()

restas()


