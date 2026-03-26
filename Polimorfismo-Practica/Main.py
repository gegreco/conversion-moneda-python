from Clases.Gato import Gato
from Clases.Perro import Perro
from Clases.Vaca import Vaca

#POLIMORFISMO: capacidad de los objetos de diferentes clases de responder al mismo metodo de forma distinta

def hacer_sonido_de_animal(animal):
    print(f"{animal.nombre} hace {animal.hacer_sonido()}")

perro = Perro("Tikka")
gato = Gato("Pelusa")
vaca = Vaca("Lechera")

hacer_sonido_de_animal(perro)
hacer_sonido_de_animal(gato)
hacer_sonido_de_animal(vaca)