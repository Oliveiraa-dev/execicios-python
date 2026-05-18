# recursos publicos e privados

class conta:
    def __init__(self,numero_agencia, saldo=0):
        self._saldo = saldo    # variavel privada por que esta iniciando ( _ )
        self.numero_agencia = numero_agencia

    def depositar(self, valor):
        #...
        self._saldo += valor

    def sacar(self, valor):
        #...
        self._saldo -= valor

    def mostrar_saldo(self):
        #...
        return self._saldo

conta = conta("0001", 100)
conta.depositar(100)
print(conta.numero_agencia)
print(conta.mostrar_saldo())