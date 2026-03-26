# ---------------------------------------------
# Listas [Coleccion de elementos mutables y ordenados]
# ---------------------------------------------

        #indices
#nombre    0(-6)      1(-5)    2(-4)     3(-3)        4(-2)     5(-1)
lista = ["manzana", "banana", "pera", "mandarina", "frutilla", "anana"]
print(lista[0:5])

if "mandarina" in lista:
    print("Si, mandarina está en la lista")

lista [1] = "platano"
lista [4] = "fresa"
lista [5] = "piña"
print(lista)

lista.insert(2, "palta")
print(lista)

lista.append("aguacate")
print(lista)

lista2 = ["ciruela", "durazno", "limon"]
lista.extend(lista2)
print(lista)

lista.remove("pera") #borra sólo la primer ocurrencia del valor
print(lista)

lista.pop(3)
print(lista)

del lista[3]
print(lista)

lista.clear
print(lista)