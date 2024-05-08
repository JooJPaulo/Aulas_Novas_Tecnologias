class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def dados_cliente(self):
        return f"Nome: {self.nome} {self.sobrenome}, CPF: {self.cpf}"
