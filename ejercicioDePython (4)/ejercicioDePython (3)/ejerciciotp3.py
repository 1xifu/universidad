"""
ejercicio 3: buscar elementos en lista (while)

crea una funcion que, utilizando while, reciba una lista y un numero, y verifique si el numero esta en la lista

"""

def BuscarElementos(lista, num):
    i = 0
    while i < len(lista):
        if lista[i] == num:
            return True
        i+=1
    return False

numeros=[3, 7, 1, 0, 99]

print(BuscarElementos(numeros, 99))

 #tomar el resultado de una funcion y pasarlo a otra funcion 