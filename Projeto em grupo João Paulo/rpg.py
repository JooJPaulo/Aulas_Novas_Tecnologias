import random

class Protagonista():
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.missoes = []

    def atacar(self, inimigo):
        dano = max(self.ataque - inimigo.defesa, 0)
        inimigo.vida -= dano
        print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano")

    def defender(self, inimigo):
        dano = max((inimigo.ataque - self.defesa) // 2, 0)
        self.vida -= dano
        print(f"{inimigo.nome} atacou {self.nome} e causou {dano} de dano")

    def curar(self):
        self.vida += 10
        print(f"{self.nome} curou 10 pontos de vida. Vida atual: {self.vida}")

    def pegar_missao(self, missao):
        self.missoes.append(missao)
        print(f"{self.nome} pegou a missão {missao.nome}")

    def concluir_missao(self, missao):
        if missao in self.missoes:
            missao.concluir(self)
            self.missoes.remove(missao)
            print(f"{self.nome} concluiu a missão {missao.nome}")
        else:
            print(f"{self.nome} não possui a missão {missao.nome}")

class Inimigo():
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, protagonista):
        dano = max(self.ataque - protagonista.defesa, 0)
        protagonista.vida -= dano
        print(f"{self.nome} atacou {protagonista.nome} e causou {dano} de dano")

class Missao():
    def __init__(self, nome, descricao, recompensa):
        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa

    def concluir(self, protagonista):
        protagonista.vida += self.recompensa
        print(f"{protagonista.nome} concluiu a missão {self.nome} e ganhou {self.recompensa} de vida")

class Catacumba:
    def __init__(self, nome, nivel, inimigos, tesouros):
        self.nome = nome
        self.nivel = nivel
        self.inimigos = inimigos
        self.tesouros = tesouros

    def explorar(self, protagonista):
        for inimigo in self.inimigos:
            while inimigo.vida > 0 and protagonista.vida > 0:
                print("\nEscolha uma ação:")
                print("1. Atacar")
                print("2. Defender")
                print("3. Curar")
                escolha = input("Digite o número da ação: ")
                
                if escolha == "1":
                    protagonista.atacar(inimigo)
                elif escolha == "2":
                    protagonista.defender(inimigo)
                elif escolha == "3":
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
            print(f"{protagonista.nome} explorou a {self.nome} e encontrou {self.tesouros}")
        else:
            print(f"{protagonista.nome} não conseguiu explorar a {self.nome}")

if __name__ == '__main__':
    nomeProtagonista = input("Digite o nome do protagonista: ")
    protagonista = Protagonista(nomeProtagonista, 100, 10, 5)
    
    inimigo1 = Inimigo("Dragão", 50, 15, 5)
    inimigo2 = Inimigo("Esqueleto", 30, 10, 3)
    
    missao1 = Missao("Derrotar o Dragão", "Derrote o dragão que está atacando a cidade", 50)
    missao2 = Missao("Explorar as Catacumbas Amaldiçoadas", "Explore as catacumbas e derrote os inimigos", 30)
    
    catacumba = Catacumba("Catacumbas Amaldiçoadas", 1, [inimigo1, inimigo2], "Tesouro Antigo")
    
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
                protagonista.pegar_missao(missoes_disponiveis[escolha_missao])
                if missao1 in protagonista.missoes:
                    catacumba.explorar(protagonista)
                    protagonista.concluir_missao(missao1)
                elif missao2 in protagonista.missoes:
                    catacumba.explorar(protagonista)
                    protagonista.concluir_missao(missao2)
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite o número da missão ou 'sair'.")
