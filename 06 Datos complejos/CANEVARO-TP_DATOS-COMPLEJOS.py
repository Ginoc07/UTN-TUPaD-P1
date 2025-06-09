#Ejercicio 1


precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

#Las nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Ejercicio 2
# (Precios actualizados)
precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450}


precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1700
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Ejercicio 3

frutas = {'Banana', 'Ananá', 'Melón', 'Uva', 'Naranja', 'Manzana', 'Pera'}

print(frutas)

#Ejercicio 4

contactos = {}

for _ in range(5):
    nombre = input("Ingrese nombre del contacto: ")
    numero = input("Ingrese número telefónico: ")
    contactos[nombre] = numero

nombre_busqueda = input("Escriba el nombre a buscar: ")
if nombre_busqueda in contactos:
    print(f"El número de {nombre_busqueda} es {contactos[nombre_busqueda]}")
else:
    print("No se ha encontrado el contacto")

#Ejercicio 5

frase = input("Ingrese una frase: ")

palabras = frase.split()
#El uso del set
palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print(f"Palabras únicas: {palabras_unicas}")
print(f"Recuento: {recuento}")

#Ejercicio 6

alumnos = []

for _ in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = tuple(float(input(f"Ingrese la nota {i+1} de {nombre}: ")) for i in range(3))
    alumnos.append((nombre, notas))

for nombre, notas in alumnos:
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio:.2f}")

#Ejercicio 7

parcial1 = {'Juan', 'María', 'Pedro', 'Angie', 'Axel'}
parcial2 = {'María', 'Axel', 'James', 'Angie', 'Sofía'}

# probaron ambos parciales
ambos_parciales = parcial1 & parcial2
print("Estudiantes que aprobaron ambos parciales:", ambos_parciales)

#aprobaron solo uno de los dos parciales 
solo_uno = parcial1 ^ parcial2
print("Estudiantes que aprobaron solo un parcial:", solo_uno)

#aprobaron al menos un parcial
todos_aprobados = parcial1 | parcial2
print("Todos los estudiantes que aprobaron al menos un parcial:", todos_aprobados)

#Ejercicio 8

inventario = {}

def consultar_stock(p): return inventario.get(p, "No existe.")
def agregar_stock(p, c): inventario[p] = inventario.get(p, 0) + c; return f"Stock de {p}: {inventario[p]} unidades"
def agregar_producto(p, c): return "Ya existe." if p in inventario else agregar_stock(p, c)

while True:
    opc = input("\n1. Consultar\n2. Agregar stock\n3. Agregar nuevo producto\nElige opción: ")
    if opc == "1": print(consultar_stock(input("Producto: ")))
    elif opc == "2": print(agregar_stock(input("Producto: "), int(input("Cantidad: "))))
    elif opc == "3": print(agregar_producto(input("Producto: "), int(input("Cantidad: "))))
    break

#Ejercicio 9

agenda = {}

def agregar_evento(dia, hora, evento):
    agenda[(dia, hora)] = evento
    return f"Evento '{evento}' agregado el {dia} a las {hora}."

def consultar_evento(dia, hora):
    return agenda.get((dia, hora), "No hay eventos programados.")

while True:
    opc = input("\n1. Agregar evento\n2. Consultar evento\nElige opción: ")
    if opc == "1":
        d, h = input("Día: "), input("Hora: ")
        e = input("Evento: ")
        print(agregar_evento(d, h, e))
    elif opc == "2":
        d, h = input("Día: "), input("Hora: ")
        print(consultar_evento(d, h))
    break

#Ejercicio 10

paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Francia': 'Paris',
    'Colombia': 'Bogotá',
    'Suecia': 'Estocolmo'
}

# Inversión del diccionario
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

print("Diccionario original:")
print(paises_capitales)

print("\nDiccionario invertido:")
print(capitales_paises)











