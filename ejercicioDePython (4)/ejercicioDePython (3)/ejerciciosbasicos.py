"""
Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética  (3+22⋅5)2 .
"""
#print (((3 + 2) / (2 * 5)) ** 2 )       

"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.
"""

#horas = float(input("ingrese sus horas trabajas : "))
#paga = float(input("ingrese lo que gana por hora : "))

#print (f"lo que gana usted en total es : {paga * horas}")


"""
Escribir un programa que lea un entero positivo, 
, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
. La suma de los 
primeros enteros positivos puede ser calculada de la siguiente forma:

"""

#num1 = int(input("ingrese un numero entero positivo : "))

#suma1 = num1 * (num1 + 1) / 2

#print(f"la suma de los primeros numeros entero entero desde 1 hasta  {num1}, es {suma1}")
            
            
            

"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal
y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> 
es el índice de masa corporal calculado redondeado con dos decimales.

"""            

kg = float(input("ingrese su peso en kilos : ")) #formula masa corporal (peso / (estatura ^ 2)). 
metros = float(input("ingrese su estatura : "))

print(f"tu masa corporal es de : {kg / (metros ** 2):.2f}") #para redondear se tiene que ocupar siempre el .2f o dependiendo la cantidad de numero que quieren redondear


"""

"""

