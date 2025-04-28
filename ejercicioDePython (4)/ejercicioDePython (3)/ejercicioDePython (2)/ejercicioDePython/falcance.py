

'''
funciones definidas por el usuario
'''

#simple 

#def greet():
#    print("hola, Python")

#greet()   

# con retorno 

#def return_greet():
#    return "hola, Python!"

#print(return_greet())



# con argumento 

#def arg_greet(name):
#    print(f"hola,{name}!")

#arg_greet(" pedro ")

# con argumentos

#def arg_greet(greet, name ):
#    print(f"hola,{greet},{name}!")

#arg_greet("hi", "pedro")

#con argumentos y retorno

def retono_argu_saludar(saludo,name):
    return(f"{saludo},{name}")


print(retono_argu_saludar("hola", "pedro"))


# con retorno de varios valores

def multiple_retorno_saludo():
    return"hola", "python"

saludo, nombre = multiple_retorno_saludo()
print(saludo)
print(nombre)

# funciones con un numero variable de argumentos 


def variable_arg_greet(*names):
    for name in names:
        print(f"hola, {name}!")
        
variable_arg_greet("python", "pedro", "fierro", "xifu" )


#funciones con un numero de variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"hola, {value} {key}!")
        
        
variable_key_arg_greet(
            languaje="python", 
            name="pedro", 
            apellido="fierro", 
            edad=36
)



"""
funciones dentro de funciones

"""

def funcion_externa():
    def funcion_interna():
        print ("funcion interna: hola, python !")
    funcion_interna()
    
        
funcion_externa()



"""
funciones del lenguaje (built-in)

"""

print(len("pedro")) #len se ocupa para saber cuantos elementos hay dentro 
print(type(36)) #para saber el tipo de variable 
print("pedro". upper())


"""
variables locales y globales

"""

globalVariable= "python"
print(globalVariable)


"""
extra

"""


def print_nums(texto1, texto2)-> int:
    cont = 0
    
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(texto1 + texto2)
        if number % 3 == 0:
            print(texto1)
        elif number % 5 == 0:
            print(texto2)

        else:
            print(number)
            cont += 1
    return cont
        
        
print(print_nums("fizz", "buzz"))