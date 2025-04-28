"""
escribre un programa que permita generar la tabla de multiplicar de un numero entero
positivo N, comenzando desde el 1.

si el usario escribe un numero incorrecto, el programa no se ejecuta. en cambio,
pregunta de nuevo por la informacion hasta que el dato ingresado sea correcto


comprobar = True

while comprobar == True:
    
        num1 = int(input("ingrese un numero entero positivo porfavor : "))

        if num1 > 0:
            
            for i in range (1,11):
            
                print(f"la multiplacion de {num1} es :  {num1 * i}  ")
            comprobar == False
        
        else:
            print("el numero ingresado no es correcto. intentelo nuevamente.")

"""

"""
escriba un programa que, al recibir como dato un numero entero positivo N
calcule el resultado de la siguiente serie:
1 + (1/2) + (1/3) + (1/4) + .... + (1/N)

si el usuario escribe un numero incorrecto, el programa no se ejecuta. en cambio,
pregunta de nuevo por la informacion que el dato ingreaso sea correcto

"""
# comprobar= True

# while comprobar == True:
#     num = int(input("ingrese un numero entero positivo : "))

#     if num > 0:
#         resultado = 0
                
#         for i in range (1,num+1): #siempre poner un +1 para que pueda sumarle un numero mas y no se quede en el ultimo numero que puso el usuario
                
#                 resultado += (1/i)
#         print(f"el resultado es : {resultado:.2f}")
                    
#     else:
#             print("el numero ingresado no es correcto. intentelo nuevamente!.")


"""
escriba un programa que, al recibir como dato un numero entero positivo N, calcule el resultado
de la siguiente serie :
1 / (1/2) * (1/3) / (1/4) * ... (*/) (1/N)
"""




#comprobar = True

# while comprobar == True:
    
#     n = int(input("ingrese un numero entero positivo: "))
#     if n > 0:
#             comprobar = False
#             resultado = 1
#             for i in range(2,n+1):
#                 if i % 2 == 0:
#                     resultado = resultado / (1/i)
#                 else:
#                     resultado = resultado * (1/i)
#             print(f"el resultado de la serie es: {resultado:.2f}")
            
                    
            
#     else:
#             print("el numero ingresado no es correcto. intentelo de nuevo. ")

"""
construya un programa que , al recibir como datos N numeros naturales, determine 
cuantos de ellos son positos, negativos o nulos.

si el usuario escribe un numero incorrecto, el programa no se ejecuta. en cambio,
pregunta de nuevo por la informacion hasta que el dato ingresado sea correcto.

"""
# comprobar = True

# while comprobar == True:
#         n = int(input("ingrese la cantidad de datos que desea procesar: "))
        
#         if n > 0:
            
#             comprobar = False
            
#             positivos = 0
#             negativos = 0
#             nulos = 0
            
#             for i in range (n):
                
#                 dato = int(input("ingrese un numero natural: "))
                
#                 if dato > 0:
#                     positivos += 1
                
#                 elif dato < 0:
#                     negativos += 1
                    
#                 else:
#                     nulos += 1
                    
#             print(f"la cantidad de numero positivos fue: {positivos}\nla cantidad de numero negativos fue: {negativos}\nla cantidad de numeros nulos fue: 5{nulos}")
#         else:
#             print("el numero ingresado no es correcto. intentelo nuevamente.")



"""
construya un programa que, al recibir como datos el peso, la altura y el genero de n personas
que ternecen a un estado de un pais, obtenga el promedio del peso y el promedio
de la altura, tanto la poblacion masculina como de la femenina.
 
"""

comprobar = True

while comprobar:
    n = int(input("Ingrese la cantidad de personas a evaluar: "))
    
    if n > 0:
        comprobar = False

        pesoHombres = alturasHombres = pesoMujeres = alturasMujeres = 0
        cantidadHombres = cantidadMujeres = 0

        for _ in range(n):
            peso = float(input("Ingrese el peso en kg: "))
            altura = int(input("Ingrese la altura en cm: "))

            while True:
                genero = input("Ingrese el género de la persona (M/F): ").upper()
                
                if genero == "M":
                    pesoHombres += peso
                    alturasHombres += altura
                    cantidadHombres += 1
                    break
                elif genero == "F":
                    pesoMujeres += peso
                    alturasMujeres += altura
                    cantidadMujeres += 1
                    break
                else:
                    print("El género ingresado no es correcto. Inténtelo nuevamente.")

        # Cálculo de promedios solo si hay hombres o mujeres
        promedioPesoH = pesoHombres / cantidadHombres if cantidadHombres else 0
        promedioAlturaH = alturasHombres / cantidadHombres if cantidadHombres else 0
        promedioPesoM = pesoMujeres / cantidadMujeres if cantidadMujeres else 0
        promedioAlturaM = alturasMujeres / cantidadMujeres if cantidadMujeres else 0

        print(f"""
De los datos obtenidos, los promedios son los siguientes:
- Promedio peso de hombres: {promedioPesoH:.2f} kg
- Promedio altura de hombres: {promedioAlturaH:.2f} cm
- Promedio peso de mujeres: {promedioPesoM:.2f} kg
- Promedio altura de mujeres: {promedioAlturaM:.2f} cm
""")
    else:
        print("El número ingresado no es correcto. Inténtelo nuevamente.")

