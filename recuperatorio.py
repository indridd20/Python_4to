#Ticiana Passalacqua Gyurkovits
while True:
        try:
            cantidadnomb = int(input("cuantos nombres quiere ordenar alfabeticamente: "))
            i = 0
            listanombre = []

            for i in range (cantidadnomb):

    
            
                nombre = str(input(f"ingrese el {i+1} nombre: "))
                listanombre.append(nombre)

            break

        except ValueError:
           print("el dato ingresado no es valido, por favor intente de nevo")

listanombre.sort
print(f"los nombres ordenados alfabeticamente son: {listanombre}")

