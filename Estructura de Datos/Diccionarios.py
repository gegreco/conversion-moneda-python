# ---------------------------------------------
# DICCIONARIO {coleccion no ordenada de pares clave-valor}
# ---------------------------------------------

diccionario = {
    "nombre": "Gabriel Greco",
    "edad": 43,
    "ciudad": "Mercedes",
    "tecnologias": ["Python", "Javascript"]
}
print(diccionario)
print(diccionario["nombre"])

claves = diccionario.keys()
print(claves)

valores = diccionario.values()
print(valores)

items = diccionario.items()
print(items)

diccionario["nombre"] = "Paco Perez"
print(diccionario)

diccionario.update({"nombre": "Paco Perez"})
print(diccionario)

diccionario["equipo"] = "Boca"
print(diccionario)

del diccionario["ciudad"]
print(diccionario)

diccionario2 = diccionario.copy()
print(diccionario2)

for x in diccionario:
    print(x)

for x,y in diccionario.items():
    print(x,y)

print("--------------------------------------------")


#DICCIONARIOS ANIDADOS

familia = {
    "padre":{
        "nombre": "Raul",
        "profesion": "mecanico"
    },
    "madre":{
        "nombre": "Leticia",
        "profesion": "periodista"
    },
    "hijo":{
        "nombre": "Alfredo",
        "profesion": "heladero"
    }
}
print(familia["padre"]["profesion"])

for pariente, data in familia.items():
    print(pariente)

    for clave in data:
        print(clave + ":", data[clave])