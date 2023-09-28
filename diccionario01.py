usuarios = {}
print(usuarios)

def registrar_usuario():
    nombreUsuario = input("ingrse un nombre de usuario: ")
    if nombreUsuario in usuarios:
        print("El usuario ya existe, intente con otro nombre")
    else:
        contraseña = input("ingrese una contraseña: ")
        usuarios[nombreUsuario] = contraseña
        print("Usuario registrado con exito.")

def iniciar_sesion():
    nombreUsuario = input("ingrse su nombre de usuario: ")
    contraseña = input("ingrese su contraseña: ")

    if nombreUsuario in usuarios and usuarios[nombreUsuario] == contraseña:
        print("Inicio de sesion exitoso. ¡Bienvenido", nombreUsuario, "!")
    else:
        print("Credenciales incorrectas. Intente nuevamente")

def menu():
    opciones = '''
    ================================================
    =   BIENVENIDOS- INICIAR SESION O REGISTRARSE  =
    ================================================
    =            1- INICIAR SESION                 =
    =            2- REGISTRARSE                    =
    =            3- SALIR                          =
    ================================================
    '''
    print(opciones)

while True:
    menu()

    opcion = input("Ingrese la opcion que desee realizar: ")

    if opcion == '1':
        iniciar_sesion()
    
    elif opcion == '2':
        registrar_usuario()

    elif opcion == '3':
        break

    else:
        print("La opcion ingresada no es valida. Intentar de nuevo")