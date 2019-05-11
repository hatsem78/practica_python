import os

work_file = open("file.txt", "r")

texto = work_file.read()

work_file.close()

print(texto)


work_file = open("file.txt", "r")

#guarda la información en un lista
lista_texto = work_file.readlines()

work_file.close()

print(lista_texto)

