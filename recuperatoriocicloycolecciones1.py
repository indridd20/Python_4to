 #Ticiana Passalacqua e Ingrid Torres

import math 

print("Este programa calcula el area de la figura que usted elija")

Menu = '''
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                          1 .TRIANGULO EQUILATERO                   "
"                          2 .CIRCUNFERENCIA                         "
"                          3 .SALIR                                  "
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''

while True : 

    def Triangulo():
        Altura = float(input("Ingrse la altura del triangulo equilatero: "))
        Base = float(input("Ingrese la base del triangulo equilatero: "))
        Area = Altura * Base /2 
        print("El area del triangulo es: ", Area)
        menu()


    def Circunferencia():
        Radio = float(input("Ingrse el radio del circunferencia: "))
        math.pi
        Area = math.pi * Radio **2
        print("El area del circunferencia es: ", Area)
        menu()

    def menu():
        print(Menu)
        opcion = int(input("Ingrese la opcion deseada: "))
        if opcion == 1:
            Triangulo()
        elif opcion == 3:
            Circunferencia()
        elif opcion == 3:
            exit()
        else:
            print("No ingreso ninguna opcion del menu, por favor ingres de nuevo una opcion")
            menu()

print("Fin del programa")

