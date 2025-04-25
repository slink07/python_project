#fazer um simulador de dados


import random
import time



def entrada():
    print('----' * 10)
    print('Bem vindo ao Lançador de dado!')
    print('----' * 10)


def dado():
    print('----' * 10)
    numeros = random.randint(1,6)
    soltar = int(input('escolha um numero entre 1 ate 6: '))
    print('----' * 10)

    if soltar == numeros:
        print('você ganhou')
        print(f'Sua escolha foi {soltar} e o dado saiu {numeros}')

    else:
        print(f'você perdeu! \nSua escolha foi {soltar} e o dado saiu {numeros}')
        
        nov()

        
def nov():
     while True:
        dnv = input('Quer jogar novamente? (S/N): '.strip().upper())
        if dnv == "S":
            dado()
        elif dnv == "N":
            return
        else:
            print("Opção inválida! Digite S ou N. ")


def saida():
    print('----' * 10)
    print('Finalizando o programa...')
    time.sleep(1)
    print('----' * 10)


entrada()
dado()
nov()
saida()