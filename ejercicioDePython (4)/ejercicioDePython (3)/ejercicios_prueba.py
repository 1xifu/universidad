"""
Ejercicios de Python - Funciones, Condicionales, Ciclos y Listas
Ejercicio 1: Promedio de números positivos

Crea una función que reciba una lista de números, calcule el promedio solo de los números positivos y lo retorne.
Si no hay positivos, debe retornar 0.
"""
def promedio_positivos(lista):
    suma = 0
    contador = 0
    for numero in lista:
        if numero > 0:
            suma += numero
            contador += 1
    if contador == 0:
        return 0
    else:
        total = suma / contador
        return suma / contador

# Prueba
numeros = [-4, -2, -7, 0, -5, 3]
resultado = promedio_positivos(numeros)
print("Promedio de positivos:", resultado)

"""
Ejercicio 2: Clasificación de edades

Crea una función sin return que reciba una lista de edades y escriba para cada una si es 'niño', 'adolescente', 'adulto' o 'anciano'.
"""
def clasificar_edades(lista):
    for edad in lista:

        if edad >= 0 and edad <= 12:
            print(f"Edad {edad}: Niño")
        elif edad >=13 and edad <= 17:
            print(f"Edad {edad}: Adolescente")
        elif edad <= 59:
            print(f"Edad {edad}: Adulto")
        else:
            print(f"Edad {edad}: Anciano")

# Prueba
edades = [-10]
clasificar_edades(edades)

"""
Ejercicio 3: Buscar elemento en lista (while)

Crea una función que, utilizando while, reciba una lista y un número, y verifique si el número está en la lista.
"""

def buscar_numero(lista, objetivo):
    i = 0
    while i < len(lista):
        if lista[i] == objetivo:
            return True
        i += 1
    return False

# Prueba
numeros = [3, 7, 1, 9, 5]
print(buscar_numero(numeros, 9))  # True
print(buscar_numero(numeros, 2))  # False

"""
Ejercicio 4: Sumar solo los pares
Haz una función que reciba una lista de enteros y devuelva la suma de solo los números pares.

"""
def suma_pares(lista):
    suma = 0
    for num in lista:
        if num % 2 == 0:
            suma += num
    return suma

# Prueba
valores = [2, 5, 8, 7, 4]
print("Suma de pares:", suma_pares(valores))

"""
Ejercicio 5: Imprimir números hasta un negativo
Crea una función sin return que lea una lista e imprima todos los números hasta encontrar el primer número negativo.

"""

def imprimir_hasta_negativo(lista):
    for num in lista:
        print(num)
        if num < 0:
            break

# Prueba
datos = [10, 5, 3, -2, 8, 7]
imprimir_hasta_negativo(datos)

"""
Ejercicio 6: Registrar notas por consola y calcular promedio
Pide al usuario ingresar 5 notas por consola. Luego crea una función que reciba la lista de notas y retorne el promedio.

"""
def calcular_promedio(lista_notas):
    suma = 0
    for nota in lista_notas:
        suma += nota
    return suma / len(lista_notas)

# Leer notas
notas = []
for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

# Llamar función
promedio = calcular_promedio(notas)
print(f"El promedio de las notas es: {promedio:.2f}")

"""
Ejercicio 7: Clasificar productos según precio ingresado por consola
Pide al usuario ingresar precios hasta que escriba -1. Luego clasifica: Barato (< 1000), Normal (entre 1000 y 5000), Caro (> 5000).
"""
def clasificar_precios(lista_precios):
    for precio in lista_precios:
        if precio < 1000:
            print(f"Precio {precio}: Barato")
        elif precio <= 5000:
            print(f"Precio {precio}: Normal")
        else:
            print(f"Precio {precio}: Caro")

# Leer precios
precios = []
while True:
    entrada = float(input("Ingrese precio del producto (-1 para terminar): "))
    if entrada == -1:
        break
    precios.append(entrada)

# Llamar función
clasificar_precios(precios)
