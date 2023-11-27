while True:
    try:
        print("este programa va a calcular el area de 3 triangulos: ")

        base1 = float(input("Ingrese el valor de la base del primer rectangulo:"))  
        altura1 = float(input("Ingrese el valor de la altura del primer rectangulo:"))

        area1 = base1 * altura1 / 2

        print("El area del triangulo es: ", area1)
        print(f"El area del triangulo de base {base1} y altura {altura1} es igual a {area1}")


        base2 = float(input("Ingrese el valor de la base del segundo rectangulo:"))  
        altura2 = float(input("Ingrese el valor de la altura del segundo rectangulo:"))

        area2 = base2 * altura2 / 2

        print("El area del triangulo es: ", area2)
        print(f"El area del triangulo de base {base2} y altura {altura2} es igual a {area2}")

        base3 = float(input("Ingrese el valor de la base del tercer rectangulo:"))  
        altura3 = float(input("Ingrese el valor de la altura del tercer rectangulo:"))

        area3 = base3 * altura3 / 2

        print("El area del triangulo es: ", area3)
        print(f"El area del triangulo de base {base3} y altura {altura3} es igual a {area3}")

        print ("Fin del programa")
        break
    
    except ValueError:
        print("El dato ingresado es erroneo, por favor vuelva a ingresarlo correctamente")


