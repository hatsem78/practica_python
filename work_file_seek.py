from io import open

work_file = open("file.txt", "r")


#seek lee a partir de la fila que se indica
print(work_file.seek(11))

final_de_archivo = work_file.tell()

print(final_de_archivo)

#al pasar un indicador termina de leer e este punto
print(work_file.read(11))