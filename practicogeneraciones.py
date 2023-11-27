# Ingrid Aldana Torres, Ticiana Passalacqua Gyurkovits
# Escribir un programa que pida al usario un numero entero que represente la cantidad de generaciones que desee.

def generaciones(numero):
    
    asteriscos = "*"
    for i in range (numero):
        print (asteriscos)
        asteriscos = asteriscos * 2

numero = int(input("Ingrese la cantidad de generaciones que quiera representar: "))
generaciones(numero)