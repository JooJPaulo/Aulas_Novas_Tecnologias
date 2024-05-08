def adicionar_contato(nome, telefone, email):
    with open('contatos.csv', 'a') as arquivo:
        arquivo.write(f'{nome},{telefone},{email}\n')
        print('Contato adicionado com sucesso!')

def alterar_contato(nome, novo_nome, novo_telefone, novo_email):
    with open('contatos.csv', 'r') as arquivo:
        contatos = arquivo.readlines()
    with open('contatos.csv', 'w') as arquivo:
        for contato in contatos:
            nome_contato, telefone_contato, email_contato = contato.strip().split(',')
            if nome_contato == nome:
                arquivo.write(f'{novo_nome},{novo_telefone},{novo_email}\n')
                print('Contato alterado com sucesso!')
            else:
                arquivo.write(f'{nome_contato},{telefone_contato},{email_contato}\n')
        print('Contato não encontrado.')

def apagar_contato(nome):
    with open('contatos.csv', 'r') as arquivo:
        contatos = arquivo.readlines()
    with open('contatos.csv', 'w') as arquivo:
        for contato in contatos:
            nome_contato, telefone_contato, email_contato = contato.strip().split(',')
            if nome_contato != nome:
                arquivo.write(f'{nome_contato},{telefone_contato},{email_contato}\n')
        print('Contato apagado com sucesso!')

def ler_contato(nome):
    with open('contatos.csv', 'r') as arquivo:
        contatos = arquivo.readlines()
    for contato in contatos:
        nome_contato, telefone_contato, email_contato = contato.strip().split(',')
        if nome_contato == nome:
            print(f'Nome: {nome_contato}')
            print(f'Telefone: {telefone_contato}')
            print(f'Email: {email_contato}')
            break
    else:
        print('Contato não encontrado.')

def listar_contatos():
    with open('contatos.csv', 'r') as arquivo:
        contatos = arquivo.readlines()
    for contato in contatos:
        nome_contato, telefone_contato, email_contato = contato.strip().split(',')
        print(f'Nome: {nome_contato}')
        print(f'Telefone: {telefone_contato}')
        print(f'Email: {email_contato}')
        print('')

def menu():
    print('1 - Adicionar contato')
    print('2 - Alterar contato')
    print('3 - Apagar contato')
    print('4 - Ler contato')
    print('5 - Listar contatos')
    print('6 - Sair')
    opcao = input('Digite a opção desejada: ')
    return opcao

while True:
    opcao = menu()
    if opcao == '1':
        nome = input('Digite o nome: ')
        telefone = input('Digite o telefone: ')
        email = input('Digite o email: ')
        adicionar_contato(nome, telefone, email)
    elif opcao == '2':
        nome = input('Digite o nome do contato que deseja alterar: ')
        novo_nome = input('Digite o novo nome: ')
        novo_telefone = input('Digite o novo telefone: ')
        novo_email = input('Digite o novo email: ')
        alterar_contato(nome, novo_nome, novo_telefone, novo_email)
    elif opcao == '3':
        nome = input('Digite o nome do contato que deseja apagar: ')
        apagar_contato(nome)
    elif opcao == '4':
        nome = input('Digite o nome do contato que deseja ler: ')
        ler_contato(nome)
    elif opcao == '5':
        listar_contatos()
    elif opcao == '6':
        break
    else:
        print('Opção inválida!')