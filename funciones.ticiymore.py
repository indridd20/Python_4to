

print("Este programa calcula el area de la figura que usted elija")

Menu = '''
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                          1 .TRIANGULO                               "
"                          2 .CIRCUNFERENCIA                          "  
"                          3 .RECTANGULO                              "
"                          4 .SALIR                                  "  
"                                                                    "
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''
import math 
def Rectangulo():
    Altura = float(input("Ingrse la altura del rectangulo: "))
    Base = float(input("Ingrese la base del rectangulo: "))
    Area = Altura * Base 
    print("El area del rectangulo es: ", Area)

def Triangulo():
    Altura = float(input("Ingrse la altura del triangulo: "))
    Base = float(input("Ingrese la base del triangulo: "))
    Area = Altura * Base /2 
    print("El area del triangulo es: ", Area)

def Circunferencia():
    Radio = float(input("Ingrse el radio del circunferencia: "))
    math.pi
    Area = match.pi * Radio **2
    print("El area del circunferencia es: ", Area)

def menu():
    print(Menu)
    opcion = int(input("Ingrese la opcion deseada: "))
    if opcion == 1:
        Triangulo()
    elif opcion == 2:
        Rectangulo()
    elif opcion == 3:
        Circunferencia()
    elif opcion == 4:
        exit()

print("Fin del programa")