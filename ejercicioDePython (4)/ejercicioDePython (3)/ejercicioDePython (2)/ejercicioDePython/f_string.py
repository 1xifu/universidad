"""
    1-¿Qué es una f-string?

        Una f-string (o cadena formateada) es una manera de insertar valores de variables
        directamente dentro de una cadena de texto, y es muy útil cuando necesitas construir
        mensajes dinámicos o mostrar resultados de cálculos.
    
    2-Sintaxis básica de una f-string:

        f"Texto {expresión}"

    -f: Es el prefijo que le dice a Python que esta cadena es una f-string.

    -"Texto {expresión}": Dentro de las llaves {}, puedes colocar cualquier 
    expresión de Python, como variables, operaciones matemáticas, etc.
"""
#practica :)

# una simple
print(f"ejemplo 1")
nombre="lucas"
print(f"hola, {nombre} \n")

# una con operaciones

print(f"ejemplo 2")
num1=5
num2=3
print(f"La suma de {num1} y {num2} es {num1+num2} \n")

# dar forma a la salida con f-string
# A veces, quieres controlar cómo se ve el resultado (por ejemplo, cuántos decimales mostrar, alinear texto, etc.).
print(f"ejemplo 3")
precio= 12.3241
print(f"El precioes {precio:.1f} \n")

# alineacion y tamaño con f-string
# Puedes alinear el texto o los numero de manera especifica y adrle un tamaño fijo
print(f"ejemplo 4")
nombre='ana'
edad=30
print(f"{'nombre:':10} {nombre}")
print(f"{'edad:':10} {edad} \n")

# Usando alineacion con numero
# Si quieres alinear los numeros o columnas de una tabla:n
print(f"ejemplo 5")
precio1= 15.9
cantidad=4
print(f"{'el precio':<10} {'cantidad':>10} {'total':>10}")
print(f"{precio1:<10} {cantidad:>10} {precio1*cantidad:>10} \n")


"""
    Resumen como crear una f-string:

    1-escribe f antes de las comillas
    print(f"")

    2-incluir expresiones entre llaves, dentro de las llaves poner variables,
    operaciones o cualquier cosa a mostrar.
    print(f"hola")

    3-usar : para darle forma al formato, limitar numero de decimales o alinar texto.

"""