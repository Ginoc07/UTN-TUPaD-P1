#Ejercicio 1 
def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1)  

num = int(input("Ingrese un número: "))

print(f"Factoriales del 1 al {num} son: ")
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")

#Ejercicio 2 
def fibonacci_recursiva(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_recursiva(num - 1) + fibonacci_recursiva (num - 2)
    
print(fibonacci_recursiva(7))

#Ejercicio 3

def potencia(n,m):
    if m == 0:
        return 1
    else:
        return n * potencia(n,m -1)
    
print(potencia(2,3))

#Ejercicio 4

def decimal_a_binario(n):
    if n == 0:  
        return "0"
    elif n == 1:  
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)  

num = int(input("Ingrese un número entero positivo: "))

print(f"El número {num} en binario es: {decimal_a_binario(num)}")

#Ejercicio 5

def palindromo(palabra):
    
    if len(palabra) <= 1:
        return True
    
    if palabra[0] != palabra[-1]:
        return False
    

    return palindromo(palabra[1:-1])

print(palindromo("neuquen"))

#Ejercicio 6

def suma_digitos(n):
    if n == 0:  
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)  

num = int(input("Coloque un número entero positivo: "))

print(f"La suma de los dígitos de {num} es: {suma_digitos(num)}")

#Ejercicio 7

def contar_bloques(n):
    if n <= 1:
        return n
    else:
        return n + contar_bloques(n-1)

print(contar_bloques(8))

#Ejercicio 8

def contar_digito(numero,digito):
    
    if numero == 0:
        return 0
    if numero % 10 == digito: 
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
    

print(contar_digito(244253222452, 2))

