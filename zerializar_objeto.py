import pickle

class Vehiculos:

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arranca(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print('Marca: ', self.marca, '\nModelo', self.modelo)



auto1 = Vehiculos('Fiat', '128')

auto2 = Vehiculos('Ford', 'Falcon')

auto3 = Vehiculos('Ford', 'Farilian')

coches = [auto1, auto2, auto3]


work_file = open("losautos", "wb")

pickle.dump(coches, work_file)

work_file.close()

del(work_file)


work_file = open("losautos", "rb")

misCoches = pickle.load(work_file)






