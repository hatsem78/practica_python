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

    #*args puede recibir un número indeterminado de parametros
    #**kwargs recibe parametros con clave valor ejemplo {clave: valor}
    def funcion_interna(*args, **kwargs):

        #acciones adicionales
        print("vamos a realizar un cálculo")

        funcion_parametro(*args, **kwargs)

        #se agregan más funcionaledades
        print('hemos terminado el cálculo')
    return funcion_interna


@funcion_decoradora
def suma(par1, par2):

    print(par1 + par2)

@funcion_decoradora
def restas(par1, par2):
    print(par1 + par2)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))


suma(10, 6)

print()

restas(10, 2)

print()

potencia(base=5, exponente=3)


