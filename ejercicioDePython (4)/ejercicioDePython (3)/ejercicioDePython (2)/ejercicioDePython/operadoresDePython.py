'''
operadores
'''

#operadores aritmeticos 

print(f"suma: 10 + 3 =  {10 + 3}")
print(f"resta: 10 - 3 = {10 - 3}")
print(f"division: 10 / 3 = {10 / 3}")
print(f"multiplicacion: 10 * 3 = {10 * 3}")
print(f"modulo: 10 % 3 = {10 % 3}")
print(f"exponentes : 10 ** 3 = {10 ** 3}")
print(f"division entera: 10 // 3 = {10 // 3}")

#operadores de comparacion

print(f"igualdad: 10 == 3 es {10 == 3}")
print(f"desigualdad: 10 != 3 es {10 != 10}")
print(f"mayor que: 10 > 3 es {10 > 3}")
print(f"menor que: 10 < 3 es {10 < 3}")
print(f"mayor o igual que : 10 >= 10 es {10 >= 10}")
print(f"menor o igual que : 10 <= 3 es {10 <= 3}")

#operadores logicos

print (f"AND && : 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4} ") #la condicion que tiene que cumplirse es que las dos sean verdades
print (f"or || : 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4} ") #la condicion que tiene que cumplirse es que una de las dos sea verdades
print (f"NOT ! : not 10 + 3 == 14  {not 10 + 3 == 14} ")#la condicion que tiene que cumplirse para que sea verdadera es que tiene que afirmar que es falsa

#operadores de asignacion

my_number = 11 # asginacion
print(my_number)
my_number += 1 # suma y asignacion
print(my_number)
my_number -= 1 # resta y asignacion 
print(my_number)
my_number *= 2  # multiplicacion y asginacion 
print(my_number)
my_number /= 2 # division y asignacion 
print(my_number)
my_number %= 2 # modulo y asginacion
print(my_number)
my_number **= 1 # exponente y asginacion
print(my_number)
my_number //= 1 # division entera y asginacion 
print(my_number)

#operadores de identidad 

my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

#operadores de pertenencia

print(f"'u' in 'mouredev' = {'u' in 'moure'}")
print(f"'b' not in 'mouredev' = {'b' not in 'mouredev'}")

# operadores de bit

a = 10 # 1010
b = 3 # 0011

print(f"AND: 10  & 3 =  {10 & 3}") # 0010
print(f"OR: 10 ")


'''
estructuras de control
'''

#condicionales 

my_string = "brais"     

if my_string == "mouredev" : #if revisa que la primera condicion se cumpla
    print ("my_string es 'mouredev' ")
elif my_string == "brais": # elif para comprabar si la anterior fue falsa
    print("my_string es 'brais' ")
else :                      # else si ninguna de las anterior condiciones se cumple se ejecuta el else
    print ("my string no es 'mouredev' ni 'brais' ")
    

# iterativas

for i in range(11):
    print(i)
    
    
i = 0

while i <= 10:   # while es una estructura de control que repite un bloque de código mientras una condición sea verdadera.
        print(i)
        i += 1


# manejo de excepciones 

try:                     #'try, except y finally' Son partes de una estructura que se usa para manejar errores y evitar que tu programa se rompa si algo sale mal.
    print(10 / 1)
except :
    print("se ha producido un error")
finally : 
    print("ha finalizado el manejo de excepciones")        
     
     
     
        
'''
extra
'''
for number in range(10,56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)