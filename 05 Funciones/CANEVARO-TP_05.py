#Ejericicio 1 

def imprimir_hola_mundo():
    print ("Hola Mundo!")

#prog principal

imprimir_hola_mundo()

#Ejercicio 2

def saludar_usuario(nombre):
    saludo = f"Hola {nombre}!"
    return saludo
    
#prog principal

nombre_usuario = input("Ingrese su nombre: ")
mensaje_saludo = saludar_usuario(nombre_usuario)
print(mensaje_saludo) 

#Ejercicio 3 

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#prog principal
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 4

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


radio = float(input("Ingrese el radio del círculo: "))

#prog principal
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo con radio {radio} es: {area:.2f}")
print(f"El perímetro del círculo con radio {radio} es: {perimetro:.2f}")

#Ejercicio 5 
def segundos_a_horas(segundos):
    """Convierte una cantidad de segundos a horas."""
    horas = segundos / 3600
    return horas

#prog principal
try:
    segundos_totales_str = input("Ingrese la cantidad de segundos: ")
    segundos_totales = int(segundos_totales_str)
    horas_resultantes = segundos_a_horas(segundos_totales)
    print(f"{segundos_totales} segundos equivalen a {horas_resultantes} horas.")
except ValueError:
    print("¡Entrada inválida! Por favor, ingrese un número entero para los segundos.")

#Ejercicio 6
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1,11):
        resultado = i * numero
        print(resultado)

#prog principal

num = int(input("ingrese un numero:"))
tabla_multiplicar(num)

#Ejercicio 7 
def operaciones_basicas(a, b):
    """Realiza las cuatro operaciones básicas con dos números y devuelve los resultados en una tupla"""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

#prog principal
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    
    resultados = operaciones_basicas(num1, num2)
    
    
    print("\nResultados de las operaciones:")
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")
except ValueError:
    print("Error: Por favor ingrese números válidos")

#Ejercicio 8 

def calcular_imc(peso, altura):
    """Calcula el Índice de Masa Corporal (IMC)"""
    return peso / (altura ** 2)

#prog principal
try:
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    
    imc = calcular_imc(peso, altura)
    
    print(f"\nSu Índice de Masa Corporal (IMC) es: {imc:.2f}")

except ValueError:
    print("Error: Por favor ingrese valores numéricos válidos")
except ZeroDivisionError:
    print("Error: La altura no puede ser cero")

#Ejercicio 9 

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32  

#prog principal
temp_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)

print(f"{temp_celsius}°C equivale a {temp_fahrenheit}°F")

#Ejercicio 10

def calcular_promedio(a,b,c):
    media = (a + b + c) / 3
    return media

#prog principal

num = int(input("ingrese el primer numero: "))
num1 = int(input("ingrese el segundo numero: "))
num2 = int(input("ingrese el tercer numero: "))

promedio_calculado = calcular_promedio(num, num2,num2)
print("El promedio es: ", promedio_calculado)