# ---------------------------------------------
#Tuplas [Coleccion de elementos inmutables y ordenados]
# ---------------------------------------------

frutas = ("manzana", "platano", "pera")
numeros = (1,2,3)
booleanos = (True, True, False)
mixto = ("manzana", 1, True)

frutas += numeros
print(frutas)

lista_frutas = list(frutas) #convierte la tupla en una lista para poder modificarla
lista_frutas.remove("manzana") #se modifica la lista
frutas = tuple(lista_frutas) #se convierte la lista en tupla nuevamente
print(frutas)

(a, b, c, d, e) = frutas #desempaquetando la tupla
print(a)
print(b)
print(c)
print(d)
print(e)

frutas_por_2 = frutas * 2 #multiplica la informacion
print(frutas_por_2)