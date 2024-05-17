import random
from typing import List

class Protagonista:
    def __init__(self, nome: str, vida: int, ataque: int, defesa: int):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.missoes: List[Missao] = []
        self.ouro = 0

    def atacar(self, inimigo: 'Inimigo'):
        dano = max(self.ataque - inimigo.defesa, 0)
        inimigo.vida -= dano
        print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano")

    def defender(self, inimigo: 'Inimigo'):
        dano = max((inimigo.ataque - self.defesa) // 2, 0)
        self.vida -= dano
        print(f"{inimigo.nome} atacou {self.nome} e causou {dano} de dano")

    def curar(self):
        self.vida += 10
        print(f"{self.nome} curou 10 pontos de vida. Vida atual: {self.vida}")

    def pegar_missao(self, missao: 'Missao'):
        self.missoes.append(missao)
        print(f"{self.nome} pegou a missão {missao.nome}")

    def concluir_missao(self, missao: 'Missao'):
        if missao in self.missoes:
            missao.concluir(self)
            self.missoes.remove(missao)
            print(f"{self.nome} concluiu a missão {missao.nome}")
        else:
            print(f"{self.nome} não possui a missão {missao.nome}")

class Inimigo:
    def __init__(self, nome: str, vida: int, ataque: int, defesa: int):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, protagonista: Protagonista):
        dano = max(self.ataque - protagonista.defesa, 0)
        protagonista.vida -= dano
        print(f"{self.nome} atacou {protagonista.nome} e causou {dano} de dano")

class Missao:
    def __init__(self, nome: str, descricao: str, recompensa: int):
        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa

    def concluir(self, protagonista: Protagonista):
        protagonista.vida += self.recompensa
        print(f"{protagonista.nome} concluiu a missão {self.nome} e ganhou {self.recompensa} de ouro. Ouro total: {protagonista.ouro}")

class Catacumba:
    def __init__(self, nome: str, nivel: int, inimigos: List[Inimigo], tesouros: str):
        self.nome = nome
        self.nivel = nivel
        self.inimigos = inimigos
        self.tesouros = tesouros

    def explorar(self, protagonista: Protagonista):
        print(f"{protagonista.nome} está explorando a {self.nome}...")
        encontrou_inimigo = random.choice([True, False])
        
        if encontrou_inimigo:
            print(f"{protagonista.nome} encontrou um {self.inimigos[0].nome}!")
            self.batalha(protagonista, self.inimigos[0])
        else:
            ouro_encontrado = 100
            protagonista.ouro += ouro_encontrado
            print(f"{protagonista.nome} encontrou um tesouro com {ouro_encontrado} de ouro. Ouro total: {protagonista.ouro}")

    def batalha(self, protagonista: Protagonista, inimigo: Inimigo):
        while inimigo.vida > 0 and protagonista.vida > 0:
            print("\nEscolha uma ação:")
            print("1. Atacar")
            print("2. Defender")
            print("3. Curar")
            escolha = self.escolher_acao()
            if escolha == 1:
                protagonista.atacar(inimigo)
            elif escolha == 2:
                protagonista.defender(inimigo)
            elif escolha == 3:
                protagonista.curar()
            else:
                print("Escolha inválida. Tente novamente.")
                continue

            if inimigo.vida > 0:
                inimigo.atacar(protagonista)

            if protagonista.vida <= 0:
                print(f"{protagonista.nome} morreu")
                return

            if inimigo.vida <= 0:
                print(f"{inimigo.nome} morreu")

        if protagonista.vida > 0:
            print(f"{protagonista.nome} venceu a batalha contra {inimigo.nome}")
        else:
            print(f"{protagonista.nome} não conseguiu vencer a batalha")

    def escolher_acao(self):
        while True:
            try:
                escolha = int(input("Digite o número da ação: "))
                if escolha in [1, 2, 3]:
                    return escolha
                else:
                    print("Escolha inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

if __name__ == '__main__':
    nomeProtagonista = input("Digite o nome do protagonista: ")
    protagonista = Protagonista(nomeProtagonista, 100, 10, 5)
    
    inimigo1 = Inimigo("Dragão", 50, 15, 5)
    inimigo2 = Inimigo("Esqueleto", 30, 10, 3)
    
    missao1 = Missao("Derrotar o Dragão", "Derrote o dragão que está atacando a cidade", 50)
    missao2 = Missao("Explorar as Catacumbas Amaldiçoadas", "Explore as catacumbas e derrote os inimigos", 30)
    
    catacumba = Catacumba("Catacumbas Amaldiçoadas", 1, [inimigo2], "Tesouro Antigo")
    
    missoes_disponiveis = [missao1, missao2]
    
    while True:
        print("\nEscolha uma missão:")
        for i, missao in enumerate(missoes_disponiveis):
            print(f"{i + 1}. {missao.nome} - {missao.descricao}")
        
        escolha = input("Digite o número da missão ou 'sair' para encerrar: ")
        
        if escolha.lower() == 'sair':
            break
        
        try:
            escolha_missao = int(escolha) - 1
            if 0 <= escolha_missao < len(missoes_disponiveis):
                missao = missoes_disponiveis[escolha_missao]
                protagonista.pegar_missao(missao)
                if missao == missao1:
                    catacumba.inimigos = [inimigo1]
                    catacumba.batalha(protagonista, inimigo1)
                elif missao == missao2:
                    catacumba.explorar(protagonista)
                protagonista.concluir_missao(missao)
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite o número da missão ou 'sair'.")
