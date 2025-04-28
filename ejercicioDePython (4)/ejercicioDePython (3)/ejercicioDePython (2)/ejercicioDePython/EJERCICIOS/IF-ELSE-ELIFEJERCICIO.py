#1.- solicite al usario el ingreso de 2 numeros y retorne un mensaje en pantalla indicando cual es el mayor o que son iguales en el casi que asi sea
num1 = int(input("ingrese el primer numero : "))

num2 = int(input("ingrese el segundo numero : "))

if num1 > num2:
    print("el numero mayor es : ", num1)
elif num1 < num2:
    print("el numero mayor es ", num2)
else: 
    print("los dos numeros son iguales")


#2.-solicite al usario el ingreso de un numero y muestre en pantalla 


numero = int(input("ingrese un numero entero positivo : "))

#validar que el numero ingresado sea un positivo

if numero < 0:
    print("solo se permiten numeros enteros positivos para calcular su factorial. ")
else:
    #inicializar el resultado como 1, ya que el factorial de 0 es 1 
    resultado = 1
    #calcular el factorial utilizando un bucle 'for'
    for i in range (1, numero + 1):
        #imprimimos el paso a paso del proceso
        print(resultado, 'x',i,'=',resultado * i)
        resultado *=1
        

#imprimir el resultado
print(f"el factorial de {numero} es: {resultado} ")



    