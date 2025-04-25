#criar um banco simples com menus


import time

num = 0
saldo_atual = 0

def bk_cmc():
    print('--===--'* 6)
    print('Bem Vindo ao seu banco!')
    print('--===--'* 6)

def opcao():
    global saldo_atual
    while num != 4:
        print('--===--'* 6)
        print('1 => Saldo')
        print('2 => Depósito')
        print('3 => Retirar')
        print('4 => Saída')
        print('--===--'* 6)
        escolha = int(input('esolha a opção que voce deseja fazer: '))

        if escolha == 4:
            print('finalizando o sistema...')
            time.sleep(0.5)
            break
        elif escolha == 2:
            din = float(input('Digite o quanto você quer depositar: R$: '))
            saldo_atual += din
        elif escolha == 1:
            saldo()
        elif escolha == 3:
            din = float(input('quanto voce quer retirar? '))
            
            if din > saldo_atual:
                print('saldo insuficiente')
            else:
                saldo_atual -= din
                print(f'Retirada realizada! Novo saldo: R$ {saldo_atual:.2f}')

        
def saldo():
        print(f'seu saldo é R$:{saldo_atual:.2f}')
        


    
        
bk_cmc()
opcao()
