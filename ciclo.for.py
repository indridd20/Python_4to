print ("Este programa calcula el area de rectangulos y los compara.")

cantidad = int(input("Cuantos rectangulos quiere comparar? "))

for i in range (cantidad):

    base = int(input(f"ingrese la base del rectangulo {i+1}"))
    altura = int(input(f"ingrese la altura del rectangulo {i+1}"))

    area =  base * altura / 2 

    print(f"El area del rectangulo {i+1} es ", area)