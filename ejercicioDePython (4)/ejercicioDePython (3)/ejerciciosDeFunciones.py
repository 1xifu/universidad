"""
programa que tomas las tres notas de un estudiantes y diga
la nota final del curso. tenga en cuenta que la primera 
y segunda nota valen el 30% de la nota final. la tercera nota
vale el 40%
"""
# def promedio(n1,n2,n3):
#     return(n1*0.3) + (n2*0.3) + (n3*0.4)
    
# n1 = float(input("ingrese la primera nota: "))
# n2 = float(input("ingrese la primera segunda: "))
# n3 = float(input("ingrese la primera tercera: "))



# print(f"la nota final es : {n1*0.3 + n2*0.3 + n3*0.4:.2f}")


def calcularEdad(añoAactual,añoNacimiento):
    edad = añoAactual - añoNacimiento
    
    return edad

miEdad = calcularEdad
edad2 = calcularEdad
print("la edad mia es : ", calcularEdad(2025,1998))
print("la edad de mi amigo es : ", calcularEdad(2025,1990))