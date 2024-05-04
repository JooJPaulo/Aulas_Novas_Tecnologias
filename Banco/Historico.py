import datetime

class Historico():
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprimir(self):
        print(f"Data de abertura: {self.data_abertura}")
        print("Transações: ", end=" ")
        for t in self.transacoes:
            print("-", t)