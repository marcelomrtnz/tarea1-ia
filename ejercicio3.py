class CuentaBancaria:
    titular = ""
    saldo = 0

    def __init__(self, titular) -> None:
        self.titular = titular

    def mostrar_saldo(self) -> str:
        print(f"Su saldo actualmente es de: L.{self.saldo}")

    def depositar(self, cantidad) -> None:
        print("DEPOSITO")
        self.saldo = self.saldo + cantidad
        self.mostrar_saldo()

    def retirar(self, cantidad) -> None:
        print("RETIRO")
        if (( self.saldo - cantidad ) >= 0):
            self.saldo = self.saldo - cantidad 
        else:
            print("Sus fondos son insuficientes.")
        self.mostrar_saldo()

cuentaBancaria = CuentaBancaria("Blanca Olmedo")

print(cuentaBancaria.depositar(2))
print(cuentaBancaria.retirar(3))
print(cuentaBancaria.retirar(2))

