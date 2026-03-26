class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular #Usando __ (dos guiones bajos) hacemos privado el atributo
        self.__saldo = saldo_inicial

    #Setter (editor, configurador)
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Deposito de ${cantidad} exitoso!")
        else:
            print("Error: no se puede depositar saldo negativo")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se han retirado ${cantidad} exitosamente")
        else:
            print("Fondos insuficientes o cantidad invalida")

    #Getter (obtener informacion privada a traves de un metodo publico)
    def obtener_saldo(self):
        return f"El Saldo actual de la Cuenta es ${self.__saldo}"