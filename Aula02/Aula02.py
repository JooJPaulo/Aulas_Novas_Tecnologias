#Exercício 01
'''
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

# a) 
print(max(lista))

# b) 
print(min(lista))

# c) 
for i in lista:
    if i % 2 == 0:
        print(i)

# d) 
print(lista.count(lista[0]))

# e) 
media = sum(lista) / len(lista)
print(media)

# f) 
soma = 0
for i in lista:
    if i < 0:
        soma += i
print(soma)
'''

#Exercício 02
'''
import random

words = ["python", "java", "javascript", "ruby", "php", "swift", "csharp"]

word = random.choice(words)

guessed_letters = []

turns = 10

print(f"A palavra tem {len(word)} letras.")

while turns > 0:

    display_word = ''.join(letter if letter in guessed_letters else '_' for letter in word)
    print("Palavra:", display_word)
    
    if display_word == word:
        print("Parabéns! Você acertou a palavra.")
        break
    
    guess = input("Digite uma letra ou adivinhe a palavra: ").lower()
    
    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            print("Você já tentou essa letra. Tente outra.")
        elif guess in word:
            print("Letra correta!")
            guessed_letters.append(guess)
        else:
            print("Letra errada.")
            turns -= 1
    elif len(guess) == len(word) and guess.isalpha():
        if guess == word:
            print("Parabéns! Você acertou a palavra.")
            break
        else:
            print("Palavra incorreta.")
            turns -= 1
    else:
        print("Entrada inválida. Tente novamente.")
    
    print(f"Turnos restantes: {turns}")

if turns == 0:
    print("Você perdeu! A palavra era:", word)
'''

#Exercício 03

'''

'''

#Exercício 04
'''
temperaturas = [-10, -8, 0, 1, 2, 5, -2,-4]

print(f"A maior temperatura registrada foi {max(temperaturas)}°C.")
print(f"A menor temperatura registrada foi {min(temperaturas)}°C.")
print(f"A média das temperaturas registradas foi {sum(temperaturas) / len(temperaturas)}°C.")
'''

#Exercício 05
'''
lista = [9, 8, 7, 12, 0, 13, 21]
listaPares = []
listaImpares = []

for i in lista:
    if i % 2 == 0:
        listaPares.append(i)
    else:
        listaImpares.append(i)

print("Lista de números pares:", listaPares)
print("Lista de números ímpares:", listaImpares)
'''

#Exercício 06
'''
lugares_vagos = [10, 2, 1, 3, 0]

while True:
    
    sala = int(input("Digite o número da sala (ou 0 para sair): "))
    
    if sala == 0:
        print("Saindo do programa...")
        break

    if sala < 1 or sala > len(lugares_vagos):
        print("Número de sala inválido. Tente novamente.")
        continue
    
    lugares_solicitados = int(input(f"Digite a quantidade de lugares solicitados para a sala {sala}: "))

    if lugares_solicitados <= lugares_vagos[sala - 1]:
        
        lugares_vagos[sala - 1] -= lugares_solicitados
        print(f"Lugares vendidos com sucesso! Lugares vagos na sala {sala}: {lugares_vagos[sala - 1]}")
    else:
        print(f"Desculpe, não há lugares vagos suficientes na sala {sala}. Lugares vagos: {lugares_vagos[sala - 1]}")
'''

#Exercício 07
'''
grid = [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22']]

vencedor = False
velha = False
tentativas = 0

while not vencedor and not velha:
    for i in range(3):
        for j in range(3):
            print(grid[i][j], end=" ")
        print()
    posicao = input("Digite a posição: ")
    for i in range(0,3):
        for j in range(0,3):
            if grid[i][j] == posicao and tentativas % 2 == 0:
                grid[i][j] = "X"
                tentativas += 1
            elif grid[i][j] == posicao and tentativas % 2 != 0:
                grid[i][j] = "O"
                tentativas += 1
    for i in range(0,3):
        if grid[i][0] == grid[i][1] == grid[i][2] or grid[0][i] == grid[1][i] == grid[2][i]:
            vencedor = True
    if grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]:
        vencedor = True
    if tentativas == 9:
        velha = True

if vencedor:
    if tentativas % 2 == 0:
        print("O jogador 2 venceu.")
    else:
        print("O jogador 1 venceu.")

if velha:
    print("Deu velha.")
'''