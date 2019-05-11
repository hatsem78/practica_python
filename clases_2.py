
#segundo paso poder instanciar la clase y pasarle, a un metodo un parametro
#en función al parametro se comportara de una manera u otra
#cración del contructor y el encapsulamiento de una clase
#encapsulamiento es que una propiedad(variable) sea privada sin que se pueda acceder desde
#fuera del la clase


class Coche():

    #constructor de la clase
    def __init__(cls):

        #propiedades
        cls.__rueda = 4
        cls.__enMarcha = False
        cls.__largoChacis = 250
        cls.__anchoChacis = 120
        cls.__enMarcha = False

    #metodos
    def arrancar(cls, arrancar):

        cls.__enMarcha = arrancar
        if cls.__enMarcha:
            chequeo = cls.__chequeo_interno()

        if cls.__enMarcha and chequeo:
            return 'El coche esta en marcha'
        elif cls.__enMarcha and chequeo == False:
            return 'algo ha ido mal, no arranca el coche'
        else:
            return 'el coche esta parado'
    def estado(cls):
        print('el coche tiene ', cls.__rueda, 'ruedas un ancho de ', cls.__anchoChacis,
              ' y un largo de ', cls.__largoChacis
              )

    #metodo encapsulado solo se puede acceder desde la clase interna
    def __chequeo_interno(cls):
        print('realiza chequeo interno')

        cls.gasolina = 'ok'
        cls.aceite = 'ok'
        cls.puertas = 'cerrada'

        if(cls.gasolina == 'ok' and cls.aceite == 'ok' and cls.puertas == 'cerradas'):
            return True
        else:
            return False


#Primer objeto
mi_cohe = Coche()

print(mi_cohe.arrancar(True))
print(mi_cohe.estado())


#Segundo Objeto
print(mi_cohe.arrancar(False))
print(mi_cohe.estado())