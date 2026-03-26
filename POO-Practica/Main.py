
from Clases.Perro import Perro

#Creando instancias de la clase Perro
perro1 = Perro("Tikka", 2) #está llamando por detras al constructor pasandole nombre y edad
perro2 = Perro("Pampa", 7) #está llamando por detras al constructor pasandole nombre y edad

#------------------------------------------------------------------------------------------

#Usando template strings con las variables propias de la instancia de una clase (objeto)
print(f"{perro1.nombre} tiene {perro1.edad} años y dice {perro1.ladrar()}")
print(f"{perro2.nombre} tiene {perro2.edad} años y dice {perro2.ladrar()}")