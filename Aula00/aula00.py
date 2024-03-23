#Exercício 01
'''
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
produto = num1 * num2
diferenca = num1 - num2
quociente = num1 / num2

print("Soma: ", soma)
print("Produto: ", produto)
print("Diferença: ", diferenca)
print("Quociente: ", quociente)
'''
#Exercício 02
'''
quadrado = "********\n*      *\n*      *\n*      *\n********\n"
oval = "  ***  \n*     *\n*     *\n*     *\n  *** \n "
seta = "    *\n      *\n* * * * *\n      *\n    *\n"
losango = "  *  \n *** \n*****\n *** \n  *  \n"

print(quadrado)
print(oval)
print(seta)
print(losango)
'''
#Exercício 03
'''
num = int(input("Digite um número: \n"))

if num % 2 == 0:
    print("O número é par.\n")
else:
    print("O número é ímpar.\n")
'''
#Exercício 04
'''
num = int(input("Digite um número de cinco dígitos: \n"))
num = str(num)

print(num[0] + "   " + num[1] + "   " + num[2] + "   " + num[3] + "   " + num[4])
'''
#Exercício 05

num = int(input("Digite um número: \n"))
num = [int(x) for x in str(num)]

for i in range(len(num)):
    print(num[i], end="    ")