cadenaEdad = " 3.55"

enteroEdad = float(cadenaEdad)

print("numero =", enteroEdad, "tipo de variable = ", type(enteroEdad))

#operador de concatenacion (+):

nombre = "pedro" 

apellido = 'fierro'

nombreCompleto = nombre + '\t '+ apellido 
print (nombreCompleto)


#operador de repeticion (*):

nombre = "pedro\t" 
resultado = nombre * 3

print(resultado)

#operador de pertenencia (in) este operador se utilza para verificar si una subcadena esta presente en una cadena mas grande

nombreCompleto = "pedro fierro"

print("pedro" in nombreCompleto)
print("olivares" in nombreCompleto)
print("fierro"in nombreCompleto)
print(" " in nombreCompleto)

# operadores de comparacion (==,!=,<,>,<=,>=): estos operadores se utilzan para comparar dos cadenas y devuelven un valor booleano (true o false) segun el resultado de la comparacion

ciudad1 = "la serena"
ciudad2 = "coquimbo"
print(ciudad1 == ciudad2)

ciudad3 = "osorno"
ciudad4 = "la serena"
print (ciudad3 == ciudad4)

print (ciudad1 != ciudad2)
print(ciudad3 != ciudad4)

#operadores de indexacion ([]): te permite realizar operacones especificas con cadenas de texto, repetir , buscar, y comparar cadenas este operador se utilza para acceder a caracteres individuales en una cadena utilizando su indice . los indices en python comienza en 0

nombre = "teresa"
i = 1
print (nombre[0 - i])
print (nombre[2 - i])
print (nombre[4 - i])
print (nombre[5 - i])

#1.- suma de dos numeros enteros:

numero1= int(input("ingrese el primer numero entero: "))
numero2= int(input("ingrese el segundo numero entero: "))
suma = numero1 + numero2
print ("la suma es:", suma)

