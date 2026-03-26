from Clases.Personaje import Personaje


class Heroe(Personaje):
    def __init__(self, nombre, salud, poder):
        super().__init__(nombre, salud) #esto me permite asignar los valores a los atributos heredados
        self.poder = poder

    def mostrar_poder(self):
        print(f"{self.nombre} tiene el poder de {self.poder}")