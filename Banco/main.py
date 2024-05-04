import datetime

class ContaBancaria():
    def __init__(self, numero_agencia, tipo_conta, saldo, limite):
        self.numero_agencia = numero_agencia
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.limite = limite

    def consultar_saldo(self):
        return self.saldo
    
    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            return False
        else:
            self.saldo -= valor
            return True
        
    def depositar(self, valor):
        self.saldo += valor
        return True
    
    def transferir(self, valor, conta_destino):
        if valor > self.saldo + self.limite:
            return False
        else:
            self.saldo -= valor
            conta_destino.saldo += valor
            return True
        
    def obter_extrato(self):
        return f"Saldo: {self.saldo}, Limite: {self.limite}"
    
    def alterar_titular(self, novo_titular):
        self.titular = novo_titular
        return True
    
    def fechar_conta(self):
        
        
class Historico():
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprimir(self):
        print(f"Data de abertura: {self.data_abertura}")
        print("Transações: ", end=" ")
        for t in self.transacoes:
            print("-", t)

class Cliente():
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def dados_cliente(self):
        return f"Nome: {self.nome} {self.sobrenome}, CPF: {self.cpf}"
    
class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_agencia, saldo, limite, juros_mensal):
        super().__init__(numero_agencia, "Poupança", saldo, limite)
        self.juros_mensal = juros_mensal

    def calcular_juros_mensal(self, taxa_juros):
        self.saldo += self.saldo * taxa_juros
        return True
    
class contaCorrente(ContaBancaria):
    def __init__(self, numero_agencia, saldo, limite, cheque_especial):
        super().__init__(numero_agencia, "Corrente", saldo, limite)
        self.cheque_especial = cheque_especial

    def utilizar_cheque_especial(self, valor):
        if valor > self.saldo + self.limite + self.cheque_especial:
            return False
        else:
            self.saldo -= valor
        