def division(dividendo, divisor):
    try:
        resultado = dividendo/divisor
    except ZeroDivisionError:
        print("Error, no se puede dividir por cero")
        resultado = None
    return resultado

print(division(4,0))
print("Este mensaje es importantisimo")

def obtener_entero(texto):
    try:
        entero = int(texto)
    except ValueError:
        print("No se puede mapear a entero un texto")
        entero = None
    return entero

print(obtener_entero("123"))
print(obtener_entero("abc"))