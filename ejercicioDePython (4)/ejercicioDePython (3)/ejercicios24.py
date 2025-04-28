"""
ejercicios de python - funciones, condicionales, ciclos y listas 
ejercicio 1: promedio de numeros positivos
enunciado:
crea una funcion que reciba una lista de numeros, calcule el promedio solo de los numeros y los retorne. si no hay positivos, debe retornar 0

"""


def promedioPositivo(lista):
    suma=0
    contador=0
    for numero in lista:
        if (numero > 0):
            suma+= numero
            contador+=1
    if contador==0:
        return 0
    else:
        return suma/contador
    
numero = [4, 33, 5, -9, 22, -99]

print("promedio es : ", promedioPositivo(numero))
