
while True:
    try:
        print("Es un programa que calcula el area de un triangulo...")

        base = float(input("Ingrese el valor de la base:"))  
        altura = float(input("Ingrese el valor de la altura:"))

        area = base * altura / 2
        print("El area del triangulo es: ", area)
        print(f"El area del triangulo de base {base} y altura {altura} es igual a {area}")

        print ("pito")
        break

    except ValueError:
        print("El dato ingresado  no es un numero real, por favor ingrese un numero real")