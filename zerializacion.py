import pickle


#creamos un archivo binario
lista_nombre = ["pedro", "ana", "maría", "jorge"]

work_file_binary = open("lista_nombre", "wb")

pickle.dump(lista_nombre, work_file_binary)

#cerramo el archivo
work_file_binary.close()

#lo borramos de memoria
del(work_file_binary)


#leemos el archivo binario que creamos en el paso anterior
work_file_binary = open("lista_nombre", "rb")

lista = pickle.load(work_file_binary)

print(lista_nombre)



