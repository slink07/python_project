'''Lista de Tarefas – Criar um sistema de tarefas onde o usuário pode adicionar, visualizar, marcar como concluída e excluir tarefas
 salvas em um arquivo.
1️⃣ Cadastrar novo usuário
2️⃣ Fazer login
3️⃣ Listar usuários cadastrados (opcional)
4️⃣ Sair'''

import time

num = 0

def cima():

    print('='* 20)
    print('Bem Vindo ao seu login!')
    print('='* 20)

def options():
    while num != 4:
        print('='* 20)
        print('1️⃣ Cadastrar novo usuário')
        print('2️⃣ Fazer login') 
        print('3️⃣ Listar usuários cadastrados ')
        print('4️⃣ Sair')
        print('='* 20)
        escolha = int(input('esolha a opção que voce deseja fazer: '))

        if escolha == 4:
            print('finalizando o sistema...')
            time.sleep(1)
            break

        elif escolha == 1:
            nome = input('digite o nome do usuario: ')
            senha = int(input('digite a senha do usuario: '))
            print('cadastrando novo usuario...')
            time.sleep(1)

            print(f'usuario {nome} cadastrado com sucesso!')

        elif escolha == 2:
            nome = input('digite o nome do usuario: ')
            senha = int(input('digite a senha do usuario: '))
            login = nome, senha
            if nome == nome and senha == senha:
                print('login realizado com sucesso!')
            else:
                print('nome ou senha inválido')


        elif escolha == 3:
            print('listando usuarios cadastrados...')
            print(f'usuarios cadastrados:{login} ')
            time.sleep(1)


cima()
options()











