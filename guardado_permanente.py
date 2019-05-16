import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad

    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.genero, self.edad)


class ListaPersona:

    personas = []

    def __init__(self):
        try:

            listaDePersonas = open("fichero_externo", "ab+")
            listaDePersonas.seek(0)
            self.personas = pickle.load(listaDePersonas)
            print("se cargaron {} personas".format(len(self.personas)))
        except:
            print('fichero vacío')
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregar_persona(self, persona):
        self.personas.append(persona)
        self.guardar_personas_fechero()

    def mostrar_persona(self):
        for persona in self.personas:
            print(persona)

    def guardar_personas_fechero(self):
        listaPersonas = open("fichero_externo", "wb")
        pickle.dump(self.personas, listaPersonas)
        listaPersonas.close()
        del(listaPersonas)

    def mostrar_info_fichero(self):
        print("la info del fichero es: ")
        for persona in self.personas:
            print(persona)
lista_persona = ListaPersona()

p = Persona('Sandra', 'Femenino', 29)



lista_persona.agregar_persona(p)

p = Persona('Ana', 'Femenino', 29)

lista_persona.agregar_persona(p)


print(lista_persona.mostrar_persona())