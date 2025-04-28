"""
ejercicio 2: clasificacion de edades
crea una funcion sin return que reciba una lista de edades y escriba para cada una si es "niño", "adolecente", "adulto"
o "anciano".

"""

def clasificarEdad(lista):
  
    for edad in lista:
        if edad < 0:
            print(f"{edad} eres un recien nacido")
            
        elif edad > 0 and edad <=12:
            print(f"{edad} años es un niño/a")
        elif edad >= 13 and edad <=17:
            print(f"{edad} eres un adolecente")
        elif edad >= 18 and edad<=50:
            print(f"{edad} eres un adulto")
        else:
            print(f"{edad} eres un anciano")

edades= [2, 99, 13, 18, 51, 10, -50]
clasificarEdad(lista=99,13,-54)
    