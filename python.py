#python trabajo practico

def menu():
    print('''
    ,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,  1-calcular triangulo  , 
    ,  2-calcular redondo    ,
    ,  3- salir              ,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,  

    ''')
def triangulo():
    trianguloa = valor1 * valor2/2
    print(trianguloa)

def redondo():
    redondoa = 3.14* radio **2     
    print(redondoa)

    
while True:
    try:
        menu()
        eleccion = int(input("elejir entre 1 y 3: "))
        if eleccion == 1:
            valor1 = int(input("ingrese un numero "))
            valor2 = int(input("ingrese un numero "))
            print(triangulo())
        
        elif eleccion == 2:
            radio = int(input("ingrese un dato "))
            print(redondo())
        elif eleccion == 3:
            break
        else:
            print("ingrese un dato entre 1 y 3")
    except ValueError:
        print("dnv")
        
print("fin")