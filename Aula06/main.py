import datetime
from decimal import Decimal
from Cliente import Cliente
from Contas import *
from Historico import Historico

if __name__ == "__main__":  
    cliente = Cliente("João", "Silva", "123.456.789-00")
    conta = ContaCorrente("1234-5", 1000, 500, 1000)
    conta.titular = cliente
    conta.historico = Historico()
    conta.historico.transacoes.append("Depósito de R$1000")
    conta.historico.transacoes.append("Saque de R$500")
    conta.historico.imprimir()

    print(conta.obter_extrato())
    print(conta.titular.dados_cliente())
    print(conta.consultar_saldo())
    print(conta.saca(500))
    print(conta.consultar_saldo())
    print(conta.deposita(200))
    print(conta.consultar_saldo())
    print(conta.transfere_para(conta, 200))
    print(conta.consultar_saldo())
    print(conta.historico.transacoes)
    print(conta.historico.imprimir())
    print(conta.obter_extrato())
    print(conta.alterar_titular(Cliente("Maria", "Silva", "987.654.321-00")))
    print(conta.titular.dados_cliente())
    print(conta.fechar_conta())
