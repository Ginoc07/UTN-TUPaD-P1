#Ejercicio 1
edad = int(input("Ingrese su edad"))
if edad >= 18: 
    print("El usuario es mayor de edad")

#Ejercicio 2
nota = float(input("Ingrese su nota:"))
if nota >= 6:
    print("Aprobado")
else: 
    print("Desaprobado")

#Ejercicio 3 
numero = int(input("Ingrese un número par:"))
if numero % 2 == 0: 
    print("Es un número par")
else:
    print("Porfavor, ingrese un número par")

#Ejercicio 4
edad = int(input("Ingrese su edad:"))
if edad < 12:
    print("Usted es niño/a")
elif 12 <= edad < 18: 
    print("Usted es adolescente")
elif 18 <= edad < 30: 
    print("Usted es adulto/a joven")
else:
    print("Usted es adulto/a")

#Ejercicio 5
contraseña = input("Ingrese una contraseña (8-14 caracteres): ")
longitud = len(contraseña)
if 8 <= longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
import random
from statistics import mode, median, mean 
nums = {random.randint(1, 100) for i in range (50)}
m1, m2, m3 = mean(nums), median(nums), mode(nums)
sesgo = "positivo" if m1 > m2 > m3 else "negativo" if m1 < m2 < m3 else "sin sesgo"
print(f"Media: {m1:.2f}\nMediana: {m2}\nModa: {m3}\nSesgo: {sesgo}")

#Ejercicio 7
palabra = input("Ingrese una frase o palabra: ")
vocales = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
if len(palabra) > 0 and palabra[-1] in vocales:
    print(palabra + "!")
else:
    print(palabra)

#Ejercicio 8 
nombre = input("Ingrese su nombre: ")
print("Opciones disponibles:")
print("1. Nombre en MAYÚSCULAS")
print("2. nombre en minúsculas")
print("3. Nombre con formato de título")

while True:
    try:
        opcion = int(input("\nSeleccione una opción (1, 2 o 3): "))
        if opcion in [1, 2, 3]:
            break
        else:
            print("Por favor, ingrese solo 1, 2 o 3")
    except ValueError:
        print("Debe ingresar un número válido")

if opcion == 1:
    resultado = nombre.upper()
elif opcion == 2:
    resultado = nombre.lower()
else:
    resultado = nombre.title()

print("Resultado:", resultado)

#Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    categoria = "Muy leve"
elif 3 <= magnitud < 4:
    categoria = "Leve"
elif 4 <= magnitud < 5:
    categoria = "Moderado"
elif 5 <= magnitud < 6:
    categoria = "Fuerte"
elif 6 <= magnitud < 7:
    categoria = "Muy Fuerte"
else:
    categoria = "Extremo"

print(f"Un terremoto de magnitud {magnitud} se clasifica como: {categoria}")

#Ejercicio 10
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

if hemisferio not in ['N', 'S']:
    print("Hemisferio no válido. Debe ser N o S.")
elif mes < 1 or mes > 12:
    print("Mes no válido. Debe ser entre 1 y 12.")
elif dia < 1 or dia > 31:
    print("Día no válido. Debe ser entre 1 y 31.")
else:

    if (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    else:
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"
    
    
    if hemisferio == 'N':
        print(f"Actualmente es {estacion_norte} en el hemisferio norte.")
    else:
        print(f"Actualmente es {estacion_sur} en el hemisferio sur.")

