
#primera clase concepto de instancia, propiedades y metodos
class Coche():
    #propiedades
    largoChacis = 250
    anchoChacis = 120
    rueda = 4
    enMarcha = False

    #metodos
    def arrancar(cls):
        cls.enMarcha = True

    def estado(cls):

        if cls.enMarcha:
            return 'El coche esta en marcha'
        else:
            return 'el coche esta parado'


# instancia de una clase es crear un objeto
mi_cohe = Coche()

mi_cohe.arrancar()

print(mi_cohe.estado())
