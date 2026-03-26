# ---------------------------------------------
# CONJUNTO o SET {coleccion no ordenada y mutable de elementos unicos}
# ---------------------------------------------

#IMPORTANTE: que sea NO ORDENADA quiere decir que NO tiene indice

conjunto_frutas = {"manzana", "platano", "pera", "piña"}
conjunto_tropicales = {"piña", "mango", "papaya"}

#conjunto_frutas.add("mandarina")
#print(conjunto_frutas)

#conjunto_frutas.update(conjunto_tropicales)
#print(conjunto_frutas)

union = conjunto_frutas | conjunto_tropicales
print(union)

interseccion = conjunto_frutas & conjunto_tropicales
print(interseccion)

difference  = conjunto_frutas - conjunto_tropicales
print(difference)