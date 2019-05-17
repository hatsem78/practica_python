import re

cadena = "vamos a aprender expreciones regulares en Python. Python es un lenguage sensillo"

print(re.search("aprender", cadena))

if re.search("aprender", cadena) is not None:
    print("no se encontro el texto")
else:
    print("Encontro el texto")

texto_encontrado = re.search("aprender", cadena)

print(texto_encontrado.start(), texto_encontrado.end(), texto_encontrado.span())

texto_encontrado = re.findall('Python', cadena)

print(texto_encontrado)


#anclas regex

lista_nombre = ['Ana Gomez', 'María Martín', 'Sandra López', 'Santiago Martín']

for elemento in lista_nombre:
    #busca al comienzo ^
    if re.findall('^Sandra', elemento):
        print(elemento)
    #busca al final $
    if re.findall('Martín$', elemento):
        print(elemento)
    print()
    if re.findall('[ez]', elemento):
        print(elemento)
lista_nombre = ['mujeres', 'hombres', 'niñas', 'niños']


for elemento in lista_nombre:

    if re.findall('niñ[oa]s', elemento):
        print(elemento)

#rangos en regex
print("===="*3, "rango en regex",'===='*3)


lista_nombre = ['Ana', 'Pedro', 'María', 'Rosa', 'Sandra', 'Cecilia']


for elemento in lista_nombre:

    if re.findall('[o-s]$', elemento):
        print(elemento)

lista_nombre = ['Ma1', 'Se1', 'Ma2', 'Ba1', 'Ma3', 'Va1', 'Va2', 'ma4']


for elemento in lista_nombre:

    if re.findall('Ma[0-3]', elemento):
        print(elemento)
    #para negar los rangos es con ^
    if re.findall('Ma[^0-3]', elemento):
        print(elemento)

#rangos en regex
print("===="*3, "rango en regex match",'===='*3)

lista_nombre = ['Ana Gomez', 'Martin Potro', 'María Martín', 'Sandra López', 'Santiago Martín', 'maría Catinga']

#la funcion match siempre empieza la búsqueda por el inicio
for elemento in lista_nombre:

    #en esta condición distingue entre mayusculas y minusculas
    if re.match('María', elemento):
        print(elemento)

    #resultado seria Dos
    if re.match('María', elemento, re.IGNORECASE):
        print(elemento)

    # comodín punto(.)
    if re.match('.ar', elemento, re.IGNORECASE):
        print(elemento)
print("===="*3, "rango en regex search", '===='*3)

lista_nombre = ['Ana Gomez', 'Martín Genial', 'Martín Potro', 'María Martín', 'Sandra López', 'Santiago Martín', 'maría Catinga']

#la funcion search busca en toda la cadena del texto
for elemento in lista_nombre:

    #en esta condición distingue entre mayusculas y minusculas
    if re.search('Martín', elemento):
        print(elemento)

