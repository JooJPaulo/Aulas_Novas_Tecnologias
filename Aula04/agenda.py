def menu():
    print('1 - Inserir contato')
    print('2 - Alterar contato')
    print('3 - Apagar contato')
    print('4 - Ler contato')
    print('5 - Listar todos os contatos')
    print('6 - Sair')
    opcao = input('Digite a opção desejada: ')
    return opcao

contatos = []

def grava(nome, telefone):
    contatos.append({'nome': nome, 'telefone': telefone})

def altera(nome, novo_nome, novo_telefone):
    for contato in contatos:
        if contato['nome'] == nome:
            contato['nome'] = novo_nome
            contato['telefone'] = novo_telefone
            print("Contato alterado com sucesso!")
            return
    print("Contato não encontrado.")

def apaga(nome):
    for contato in contatos:
        if contato['nome'] == nome:
            contatos.remove(contato)
            print("Contato apagado com sucesso!")
            break

def le(nome):
    for contato in contatos:
        if contato['nome'] == nome:
            print(f'Nome: {contato["nome"]}')
            print(f'Telefone: {contato["telefone"]}')
            break

def lista():
    for contato in contatos:
        print(f'Nome: {contato["nome"]}')
        print(f'Telefone: {contato["telefone"]}')
        print('')

while True:
    opcao = menu()
    if opcao == '1':
        nome = input('Digite o nome: ')
        telefone = input('Digite o telefone: ')
        grava(nome, telefone)
    elif opcao == '2':
        nome = input('Digite o nome do contato que deseja alterar: ')
        novo_nome = input('Digite o novo nome: ')
        novo_telefone = input('Digite o novo telefone: ')
        altera(nome, novo_nome, novo_telefone)
    elif opcao == '3':
        nome = input('Digite o nome do contato que deseja apagar: ')
        apaga(nome)
    elif opcao == '4':
        nome = input('Digite o nome do contato que deseja ler: ')
        le(nome)
    elif opcao == '5':
        lista()
    elif opcao == '6':
        break
    else:
        print('Opção inválida!')