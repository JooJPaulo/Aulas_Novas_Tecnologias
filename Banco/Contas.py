from decimal import Decimal
import datetime

class ContaBancaria:
    def __init__(self, numero_agencia, tipo_conta, saldo=0, limite=0):
        self.numero_agencia = numero_agencia
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.limite = limite
        self.titular = None

    def consultar_saldo(self):
        return self.saldo

    def saca(self, valor):
        if valor > self.saldo + self.limite:
            return False
        else:
            self.saldo -= valor
            return True

    def deposita(self, valor):
        self.saldo += valor
        return True

    def transfere_para(self, destino, valor):
        if self.saca(valor):
            destino.deposita(valor)
            return True
        else:
            return False

    def obter_extrato(self):
        extrato = f"Número da Agência: {self.numero_agencia}\n"
        extrato += f"Tipo de Conta: {self.tipo_conta}\n"
        extrato += f"Saldo: {self.saldo}\n"
        extrato += f"Limite: {self.limite}\n"
        return extrato

    def alterar_titular(self, novo_titular):
        self.titular = novo_titular
        return True

    def fechar_conta(self):
        if self.saldo > 0:
            if self.titular:
                if hasattr(self.titular, 'deposita'):
                    self.titular.deposita(self.saldo)
        self.saldo = 0
        return True

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_agencia, saldo, limite, juros_mensal):
        super().__init__(numero_agencia, "Poupança", saldo, limite)
        self.juros_mensal = Decimal(juros_mensal)

    def calcular_juros_mensal(self):
        self.saldo += self.saldo * self.juros_mensal
        return True

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_agencia, saldo, limite, cheque_especial):
        super().__init__(numero_agencia, "Corrente", saldo, limite)
        self.cheque_especial = Decimal(cheque_especial)

    def utilizar_cheque_especial(self, valor):
        valor = Decimal(valor)
        if valor > self.saldo + self.cheque_especial:
            return False
        else:
            self.saldo -= valor
            return True
