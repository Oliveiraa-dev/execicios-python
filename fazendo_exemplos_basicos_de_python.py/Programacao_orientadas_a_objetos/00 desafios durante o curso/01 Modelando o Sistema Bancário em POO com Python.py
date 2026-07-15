from abc import ABC, abstractmethod
from datetime import datetime


# =========================
# CLIENTE
# =========================
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


# =========================
# HISTÓRICO
# =========================
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })


# =========================
# CONTA
# =========================
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor <= 0:
            print("❌ Valor inválido")
            return False

        if valor > self._saldo:
            print("❌ Saldo insuficiente")
            return False

        self._saldo -= valor
        print("✔ Saque realizado com sucesso")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("❌ Valor inválido")
            return False

        self._saldo += valor
        print("✔ Depósito realizado com sucesso")
        return True


# =========================
# CONTA CORRENTE
# =========================
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([
            t for t in self.historico.transacoes
            if t["tipo"] == Saque.__name__
        ])

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("❌ Saque acima do limite permitido")
            return False

        if excedeu_saques:
            print("❌ Limite de saques excedido")
            return False

        return super().sacar(valor)

    def __str__(self):
        return f"""
Agência:\t{self.agencia}
Conta:\t\t{self.numero}
Titular:\t{self.cliente.nome}
Saldo:\t\tR$ {self.saldo:.2f}
"""


# =========================
# TRANSAÇÕES
# =========================
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self._valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self._valor):
            conta.historico.adicionar_transacao(self)