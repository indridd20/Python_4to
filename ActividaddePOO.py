class Personaje1:

    def __init__(self, nombre, apellido, edad,) :
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludo1(self):
        print(f"Hola! soy {self.nombre}{self.apellido} y tengo {self.edad}años")

class Personaje2:

    def __init__(self, nombre, apellido, edad,) :
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

        def saludo2(self):
             print(f"Hola! yo soy {self.nombre}{self.apellido} y tengo {self.edad}años")

p1 = Personaje1(Alma, Moyano, 15)
p2 = Personaje2(Ingrid, Torres, 15)

Personaje1.saludo1()
Personaje2.saludo2()