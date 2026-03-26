from functools import reduce


def saludar(nombre):
    print("Hola", nombre)

saludar("Gabriel")

def mostrar_mercaderia(mercaderia):
    for item in mercaderia:
        print(item)

lista_frutas = ["manzana", "pera", "banana"]

mostrar_mercaderia(lista_frutas)

def suma(a,b):
    return a + b

print(suma(2,3))

def operaciones(a,b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b
    return(suma, resta, multiplicacion, division)

print(operaciones(4,2))

#----------------------------------------------------------------
#FUNCIONES LAMBDA

def duplicar(num):
    return num * 2
print(duplicar(5))

duplicar_lambda = lambda num: num * 2   #FUNCION LAMBDA (es lo mismo que la funcion de arriba)
print(duplicar_lambda(5))


def multiplicar(a,b):
    return a * b
print(multiplicar(5,4))

multiplicar_lambda = lambda a,b: a * b
print(multiplicar_lambda(5,4))

def operaciones(operacion):
    if operacion == "suma":
        return lambda x,y : x + y
    elif operacion == "resta":
        return lambda x,y : x - y
    elif operacion == "multiplicacion":
        return lambda x,y : x * y
    else:
        return lambda x,y : x / y

resultado = operaciones("suma")
print(resultado(10,5))
resultado = operaciones("resta")
print(resultado(10,5))
resultado = operaciones("multiplicacion")
print(resultado(10,5))
resultado = operaciones("division")
print(resultado(10,5))

#--------------------------------------------------------
#FUNCIONES COMO ARGUMENTOS (CALLBACKS)

def aplicar_funcion(func, valor):
    return func(valor)

def cuadrado(x):
    return x * x

def cubo(x):
    return x * x * x

print(aplicar_funcion(cuadrado, 3))
print(aplicar_funcion(cubo, 3))

#----------------------------------------------------------
#FUNCIONES DE ORDEN SUPERIOR

#MAP: toma una funcion y un iterable como argumentos y aplica la funcion a cada elemento del iterable

def cuadrado(x):
    return x * x

numeros = [1,2,3,4,5,6,7,8,9,10,11,12]

cuadrados = list(map(cuadrado, numeros))
cuadrados = list(map(lambda x: x * x, numeros)) #lo mismo pero en funcion lambda

print(cuadrados)


#FILTER: toma una funcion que devuelve True o False y un iterable y devuelve solo los elementos que devuelvan True como argumento de la funcion

def es_par(x):
    return x % 2 == 0

pares = list(filter(es_par, numeros))
pares = list(filter(lambda x: x%2 == 0, numeros)) #lo mismo pero en funcion lambda

print(pares)


#REDUCE: toma una funcion que reciba dos argumentos y un iterable y aplica la funcion de forma acumulativa a los elementos del iterable

def suma(x, y):
    return x + y

sumatoria = reduce(suma, numeros)

print(sumatoria)


#CLOSURE FUNCTIONS

def exterior(x):
    def interior(y):
        return x + y
    return interior

#creamos una clausura llamando a la funcion EXTERIOR
clausura = exterior(10)

#ahora cuando llamamos a la funcion clausura va a RECORDAR el valor que le dimos

resultado = clausura(5)

print(resultado)


#DECORADOR y ENVOLTORIO (DECORATOR Y WRAPPER)

def decorador(funcion):
    def envoltorio():
        print("Esta funcionalidad se dispararia antes de la funcion que nos pasen por argumento")
        funcion()
        print("Esta funcionalidad se dispararia despues de la funcion que nos pasen por argumento")
    return envoltorio

def saludar():
    print("Hola, estoy saludando")

saludo_decorado = decorador(saludar)

saludo_decorado()