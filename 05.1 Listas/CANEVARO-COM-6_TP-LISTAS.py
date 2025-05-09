#Ejercicio 1

multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

#Ejercicio 2

perifericos = ["Gaming", "Natacion", "Documentales", "Makeup", "Musica"]
print(perifericos[-2])

#Ejercicio 3

lista_palabras = []

lista_palabras.append("Lady")
lista_palabras.append("Gaga")
lista_palabras.append("Show")

print(lista_palabras)

#Ejercicio 4

animales = ["perro", "gato", "conejo", "pez"]


animales[1] = "loro"  # Índice 1 a "gato"
animales[-1] = "oso"  # Índice -1 a "pez"

print(animales)

#Ejercicio 5

#Lo que hace el programa es crear una lista de números aleatorios, y entre esos números busca el valór máximo (el más alto) y lo elimina de la lista, mostrando una lista sin ese número 

#Ejercicio 6 

numeros = list(range(10, 31, 5))

print(numeros[:2])

#Ejercicio 7

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "fiesta"
autos[2] = "cronos"

print(autos)

#Ejercicio 8

lista_dobles = []

lista_dobles.append(5 * 2)
lista_dobles.append( 10 * 2)
lista_dobles.append(15 * 2)

print(lista_dobles)

#Ejercicio 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# Agrego jugo al tercer cliente
compras[2].append("jugo")
# Reemplazo "fideos" por "tallarines" al segundo cliente
indice_fideos = compras[1].index("fideos")  
compras[1][indice_fideos] = "tallarines"  
# Elimino "pan" al primer cliente
compras[0].remove("pan")

print(compras)


#Ejercicio 10 

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)

