#criar um menu para fazer contas para vc
import math
num = 0

def calculadora(num):
    while num != 5:
        
        nmb1 = int(input('escolha um numero: '))
        nmb2 = int(input('escolha outro numero: '))
        
        print(
            "1. somar\n"
            "2. subtrair\n"  
            "3. multiplicar\n"  
            "4. dividir\n"  
            "5.sair\n")

        num = int(input('o que vc quer fazer? '))
        
        if num == 5:
            print('saindo do programa')

        elif num == 4:
            num = nmb1 // nmb2
            print(num)

        elif num == 3:
            num = nmb1 * nmb2
            print(num)
        elif num == 2:
            num = nmb1 - nmb2
            print(num)

        elif num == 1:
            num = nmb1 + nmb2
            print(num)
        else:
            print('opçao invalida')



        


print(calculadora(num))


