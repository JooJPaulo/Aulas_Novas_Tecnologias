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