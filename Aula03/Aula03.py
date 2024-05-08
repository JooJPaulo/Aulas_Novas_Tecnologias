#Exercício 01
'''
dicionario = {"B" : 1, "o" : 2, "a" : 3, " " : 4, "n" : 5, "o" : 6, "i" : 7, "t" : 8, "e" : 9, "s" : 10}

print(dicionario)
'''

#Exercício 02
'''
lista1 = [1, 2, 3, 4, 5]
lista2 = [0, 3, 4, 5, 6]

print("Valores comuns entre as listas: " + str(set(lista1) & set(lista2)))
print("Valores somente na lista1: " + str(set(lista1) - set(lista2)))
print("Valores somente na lista2: " + str(set(lista2) - set(lista1)))
print("Valores diferentes entre as listas: " + str(set(lista1) ^ set(lista2)))
'''

#Exercício 03
'''
listaOriginal = [1, 2, 3, 4, 5]
listaNova = listaOriginal.copy()

print("Valores que não foram alterados: " + str(listaOriginal))
listaNova.append(6)
print("Valores que foram adicionados na lista original: " + str(set(listaNova) - set(listaOriginal)))
listaNova.remove(1)
print("Valores que foram removidos da lista original: " + str(set(listaOriginal) - set(listaNova)))
'''

#Exercícios 04 e 05
'''
pessoa1 = {
    "first_name": "João",
    "last_name": "Silva",
    "age": 25,
    "city": "São Paulo"
}

pessoa2 = {
    "first_name": "Maria",
    "last_name": "Santos",
    "age": 30,
    "city": "Rio de Janeiro"
}

pessoa3 = {
    "first_name": "José",
    "last_name": "Oliveira",
    "age": 35,
    "city": "Curitiba"
}

people = [pessoa1, pessoa2, pessoa3]

for pessoa in people:
    print("Nome completo: " + pessoa["first_name"] + " " + pessoa["last_name"])
    print("Idade: " + str(pessoa["age"]))
    print("Cidade: " + pessoa["city"])
    print("\n")
'''

#Exercício 06
'''
bolt = {
    "Tipo": "Cachorro Salsicha",
    "Dono": "Pedro"
}

tapioca = {
    "Tipo": "Cachorro Salsicha",
    "Dono": "João"
}

pets = [bolt, tapioca]

for pet in pets:
    print("Tipo: " + pet["Tipo"])
    print("Dono: " + pet["Dono"])
    print("\n")
'''

#Exercício 07

sandwich_orders = ["Atum", "Frango", "Carne", "Queijo"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("Preparando sanduíche de " + sandwich)
    finished_sandwiches.append(sandwich)

print("\nSanduíches prontos: " + str(finished_sandwiches))