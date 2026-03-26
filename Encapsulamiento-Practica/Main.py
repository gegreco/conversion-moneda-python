from Clases.Cuenta_Bancaria import CuentaBancaria

#Creamos Instancia
cuenta = CuentaBancaria("Gabriel Greco", 1000)

#Intentamos acceder a datos privados
#print(cuenta.__saldo) #NO SE PUEDE

#Intentamos modificar el titular y el saldo en forma directa
#cuenta.__titular = "Roberto" #TAMPOCO SE PUEDE
#cuenta.__saldo = 1000000000

#print(cuenta.obtener_saldo())

#Obtener Saldo Inicial
print(cuenta.obtener_saldo())

#Depositar $500 y obtener saldo
cuenta.depositar(500)
print(cuenta.obtener_saldo())

#Retirar $1000 y obtener saldo
cuenta.retirar(1000)
print(cuenta.obtener_saldo())