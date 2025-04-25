'''===============================
    AGENDA DE CONTATOS 📱
===============================

[1] Adicionar novo contato
[2] Buscar contato
[3] Editar contato
[4] Deletar contato
[5] Listar todos os contatos
[6] Sair'''




num = 0

def inicio():
    print("=" * 30)
    print("AGENDA DE CONTATOS ")
    print("=" * 30)


def opcao():
    while num != 6:
        print('[1] Adicionar novo contato')
        print('[2] Buscar contato')
        print('[3] Editar contato')
        print('[4] Deletar contato')
        print('[5] Listar todos os contatos')
        print('[6] Sair')
        
        pergunta = int(input('Qual opção voçê deseja escolher: '))

        if pergunta == 6:
            print('saindo do programa')
            break

        elif pergunta == 1:
            nomes = input('quem vc vai adicionar: ')
            telefone = int(input('qual o número de telefone: '))
            print(f'contato adicionado com sucesso: {nomes} - {telefone}')
            contatos = {'nomme': nomes, 'telefone': telefone}
        
        elif pergunta == 5:
            print(contatos)
        
        elif pergunta == 2:
            busca = str(input('quem vc vai buscar: '))
            if busca in contatos:
                print(f'{busca} - {contatos[busca]}')
            else:
                print('contato não encontrado')




inicio()
opcao()



