'''en python, una funcion es un bloque de codigo que realiza una tarea especifica y se puede invocar desde cualquier parte del programa para realizar esa tarea.
las funciones permiten reutilizar el codigo modulizar el programa y hacerlo mas legible y mantenible'''
 
 
#def saludar():
#     print('---------------')
#     nombre = input('ingrese tu nombre: ')
#    apellido = input('ingresa tu apellido: ')
#     print('buenas tardes', nombre, apellido, '!')
#    print('-------------')
 
#saludar()

'''declaracion de una funcion:
en python, una funcion se declara utilizando la palabra clave def, seguida del nombre de la funcion, parantesis que pueden contener argumentos(parametros) de la funcion
y dos puntos, depsues, se escribe el cuerpo de la funcion, que contiene el codigo que se ejecutara cuando la funcion sea llamada
'''
'''funciones parametrizadas
las funciones parametrizadas en python son funciones que aceptan uno o mas parametros(argumentos) como entrada
estos parametros son valores '''

'''funcion con argumentos'''

def saludar(nombre, apellido):
     print("-----------")
     print('buenas tardes', nombre, apellido, "!")
     print("-----------")
     
     
nombre = input('ingrese tu nombre: ')
apellido = input('ingrese tu apellido : ')
saludar(nombre,apellido)

def agregarProducto(nombre,marca,precio):
     #preparamos una cadena con los parametros recibidos
     producto = f"{nombre} ({marca}) ==> $ {precio}"
     print(f"se ha agregado: {producto} al inventario.")
#llamamos a la funcion y pasamos los argumentos
agregarProducto("teclado","microsoft",22500)
#llamamos a la funcion y pasamos los argumentos
agregarProducto("mouse", "hp",15900)
#llamamos a la funcion y pasamos los argumentos
agregarProducto("monitor","acer",185000)