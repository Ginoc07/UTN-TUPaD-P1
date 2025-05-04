#Ejercicio 1
for i in range(0, 101):
    print(i)

#Ejercicio 2 
numero = input("Coloque un número entero: ")

# Verificar que el input sea número entero 
if numero.lstrip('-').isdigit():
    
    cantidad_digitos = len(numero.lstrip('-'))
    print(f"El número ingresado tiene {cantidad_digitos} dígitos.")
else:
    print("Error: Ingrese un número entero válido")

#Ejercicio 3
inicio = int(input("Ingresa el primer número entero: "))
fin = int(input("Ingresa el segundo número entero: "))

if inicio > fin:
    inicio, fin = fin, inicio

# Sumar enteros excluyendo los valores dados por el usuario
suma = sum(range(inicio + 1, fin))

print(f"La suma de los números enteros entre {inicio} y {fin}, excluyéndolos, es: {suma}")

#Ejercicio 4 
total = 0

print("Ingresa números enteros para sumarlos, y 0 para terminar")

while True:
    numero = int(input("Ingresa un número: "))
    if numero == 0:
        break
    total += numero
# El break es para terminar el bucle de sumar, sino no se podría terminar
print(f"La suma total es: {total}")

#Ejercicio 5
import random
def juego_adivina_numero():
    
    num_secreto = random.randint(0, 9)
    intentos = 0
    # Importar la funcón random que es la de aleatoriedad
    print("Adivina el número secreto entre 0 y 9")
    
    while True:
        try:
            
            intento = int(input("Ingresa tu numero: "))
            intentos += 1
            
            # Verificar si acertó
            if intento == num_secreto:
                print(f"Correcto el número era {num_secreto}.")
                print(f"Necesitaste {intentos} intentos.")
                break
            
            elif intento < num_secreto:
                print("El número secreto es mayor.")
            else:
                print("El número secreto es menor.")
                
        except ValueError:
            print("ingresa solo números enteros.")

juego_adivina_numero()

#Ejercicio 6

print("Números pares entre 100 y 0 de forma decreciente:")
for numero in range(100, -1, -2):
    print(numero)

#Ejercicio 7
while True:
    try:
        n = int(input("Ingrese un número positivo: "))
        if n >= 0:
            print("Suma total:", n * (n + 1) // 2)
            break
    except ValueError:
        pass

#Ejercicio 8

pares = impares = positivos = negativos = 0

for i in range(100):
    n = int(input(f"Número {i + 1}: "))
    pares += n % 2 == 0
    impares += n % 2 != 0
    positivos += n > 0
    negativos += n < 0

print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

#Ejercicio 9 
suma = 0

for i in range(100):
    n = int(input(f"Ingrese el número {i + 1}: "))
    suma += n

media = suma / 100
print(f"La media de los 10 números es: {media}")

#Ejercicio 10 

numero = input("Ingresa un número entero: ")

# Inviertir la cadena

numero_invertido = numero[::-1]
print(f"Número invertido: {numero_invertido}")

