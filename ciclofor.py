print("programa para calcular las areas")

listaArea = []
listaBase = []
listaAltura = []


cantidad = int(input("ingrese la cantidad deseada "))
 
for i in range (cantidad):

     base = int(input(f"ingrese la base del rectangulo {i+1} "))
     listaBase.append(base)

     altura = int(input(f"ingrese la altura del rectangulo {i+1} "))
     listaAltura.append(altura)


     Area = base*altura 
     listaArea = Area
     


print(listaArea)
print(listaBase)
print(listaAltura)

listaArea.sort
print("rectangulomas grande es: ", listaAltura)

print(f"El area del rectangulo de{i+1} es {Area}")


print("fin del programa")
