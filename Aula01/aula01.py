#Exercício 06
'''
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

x1 = (-b + delta**(1/2))/(2*a)
x2 = (-b - delta**(1/2))/(2*a)

print("x1 = ", x1)
print("x2 = ", x2)
'''

#Exercício 07
'''
segundos = int(input("Digite o valor em segundos: "))

dias = segundos // 86400
segundos = segundos % 86400
horas = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")
'''

#Exercício 08
'''
celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = celsius * 9/5 + 32

print("A temperatura em Fahrenheit é: ", fahrenheit)
'''

#Exercício 09
'''
menu = int(input(""" escolha uma operação:
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Sair
"""))

while menu != 5:
    if menu == 1:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        print("A soma de a e b é: ", a + b)
    elif menu == 2:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        print("A subtração de a e b é: ", a - b)
    elif menu == 3:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        print("A multiplicação de a e b é: ", a * b)
    elif menu == 4:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        print("A divisão de a e b é: ", a / b)
    else:
        print("Opção inválida")
    menu = int(input(""" escolha uma operação:
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Sair
"""))
'''

#Exercícios 10 e 11
'''
num = int(input("Digite um número: "))

if num % num == 0 and num % 1 == 0:
    print("O número", num, "é primo.")
else:
    print("O número", num, "não é primo.")
'''

#Exercício 12
'''
num = int(input("Digite um número: "))

print("Os números primos menores que", num, "são:", end=" ")

for i in range(2, num):
    primo = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i, end=" ")
'''

#Exercícios 13 e 14
'''
num = int(input("Digite um número: "))

factorial = 1
for i in range(1, num + 1):
    factorial *= i

print("O factorial de", num, "é:", factorial)
'''

#Exercício 15
'''
num = int(input("Digite um número: "))

quadrado = 0
impar = 1

for i in range(num):
    quadrado += impar
    impar += 2

print(f"O quadrado de {num} é:", quadrado)
'''

#Exercício 16
'''
n = int(input("Digite um número: "))

fibonacci = [0, 1]

while fibonacci[-1] + fibonacci[-2] <= n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print("A sequência de Fibonacci até", n, "é:", fibonacci)
'''

#Exercício 17

conta = input("Digite o número da conta (até 6 dígitos): ")

soma = sum(int(digit) for digit in conta)

digito = soma % 10

contaCompleto = f"00{conta}-{digito}"
print("Número de conta completo:", contaCompleto)
