listanumeros = []

cantidad = int(input("ingrese la cantidad de numeros que quiere ordenar: "))
i=0

for i in range (cantidad):
    while True:
        try:
            numero = int(input(f"ingrese el {i+1} numero: "))
            listanumeros.append(numero)

            break
         
        except ValueError:
            print("El dato ingresado no es un entero")

listanumeros.sort()
print(f"La lista de numeros es {listanumeros}")
