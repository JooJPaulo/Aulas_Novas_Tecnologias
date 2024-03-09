#Exercício 01

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

#Exercício 02

quadrado = "********\n*      *\n*      *\n*      *\n********\n"
oval = "  ***  \n*     *\n*     *\n*     *\n  *** \n "
seta = "    *\n      *\n* * * * *\n      *\n    *\n"
losango = "  *  \n *** \n*****\n *** \n  *  \n"

print(quadrado)
print(oval)
print(seta)
print(losango)

#Exercício 03

num = int(input("Digite um número: \n"))

if num % 2 == 0:
    print("O número é par.\n")
else:
    print("O número é ímpar.\n")

#Exercício 04

num = int(input("Digite um número de cinco dígitos: \n"))
num = str(num)

print(num[0] + "   " + num[1] + "   " + num[2] + "   " + num[3] + "   " + num[4])

#Exercício 05

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

x1 = (-b + delta**(1/2)) / (2*a)
x2 = (-b - delta**(1/2)) / (2*a)

print("x1: ", x1)
print("x2: ", x2)