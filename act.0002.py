print("Este programa calcula el area de rectangulos y los compara")

listaaltura = []
listabase = []
listaarea = []
i = 0

for i in range (3):
    print("ingrese los valores del rectangulo ", i+1)
    
    altura = float(input("Ingrese el valor de la altura del rectangulo"))
    listaaltura.append(altura)
    
    base =float(input("ingrese el valor de la base del rectangulo"))
    listabase.append(base)
    
    area=float(input("ingrese el valoe del area del rectangulo"))
    listaarea.append(area)
    
    area = base * altura 
    listaarea.append(area)

print(f"los valores de las bases son: {listabase}")
print(f"los valores de las alturas son: {listaaltura}")
print(f"los valores de las areas son: {listaarea}")

print("fin del programa") 
