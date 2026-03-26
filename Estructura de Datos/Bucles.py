# ---------------------------------------------
#BUCLES
# ---------------------------------------------

        #indices
#nombre    0(-6)      1(-5)    2(-4)     3(-3)        4(-2)     5(-1)
frutas = ["manzana", "banana", "pera", "mandarina", "frutilla", "anana"]
frutas2 = ["ciruela", "durazno", "limon"]

#bucle for
for fruta in frutas:
    print(fruta)

#bucle for con indice disponible
for i in range(len(frutas)):
    print(frutas[i])
    print(i)

#bucle while
i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1

#shorthand [abreviacion del bucle for en una sola linea]
[print(fruta) for fruta in frutas]

print("-----------------")
# ---------------------------------------------
#ABREVIACIONES
# ---------------------------------------------

#               dato a 
#nombre         asignar    bucle             condicion
frutas_con_e = [fruta for fruta in frutas if "e" in fruta] #forma abreviada del codigo escrito mas abajo

#for fruta in frutas:
#    if "e" in fruta:
#       frutas_con_e.append(fruta)

print(frutas_con_e)

print("-----------------")
# ---------------------------------------------
#ORDENAMIENTO
# ---------------------------------------------

frutas.sort()
print(frutas)

frutas.sort(reverse=True)
print(frutas)

frutas.reverse()
print(frutas)

frutas_con_mayusculas_y_minusculas = ["Manzana", "banana", "Pera", "mandarina", "Frutilla", "anana"]
frutas_con_mayusculas_y_minusculas.sort(key=str.lower)
print(frutas_con_mayusculas_y_minusculas)

print("-----------------")
# ---------------------------------------------
#COPIAR Y JUNTAR
# ---------------------------------------------

copia_frutas = frutas.copy()
print(copia_frutas)

copia2_frutas = list(frutas)
print(copia2_frutas)

frutas1_y_2 = frutas + frutas2 #joint de listas
print(frutas1_y_2)