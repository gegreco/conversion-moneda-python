from Clases.Heroe import Heroe
from Clases.Villano import Villano


superman = Heroe("Superman", 100, "Volar")
joker = Villano("Joker", 80, "Robar Bancos")

#-----------------------------------------------------------------

superman.identificarse() #Heredado
superman.mostrar_salud() #Heredado

superman.mostrar_poder() #Metodo (comportamiento) propio de Heroe

joker.identificarse() #Heredado
joker.mostrar_salud() #Heredado

joker.mostrar_habilidad() #Metodo (comportamiento) propio de Villano