#Ticiana Passalacqua Gyurkovits

print("INICIO DEL PROGRAMA")

print("Este programa ordena de menor a mayor 10 numeros a su elección")
        
i = 0

listnumeros = []

for i in range(10):

            numeros=(input(int(f"ingrese el {i+1} valor ")))

            listnumeros.append(numeros)

            listnumeros.sort(numeros)





print("El orden de los numeros es: ", numeros)

print("FIN DEL PROGRAMA")