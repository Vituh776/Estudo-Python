from time import sleep
r = 0
resuldado = 0
print('-=-' * 30)
n1 = int(input('Escolha um numero: '))
n2 = int(input('Escolha outro numero: '))
print('-=-' * 30)
sleep(1)
while r != 5:
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos numeros')
    print('[ 5 ] Sair do programa')
    r = int(input('>>>>>>>>Escolha uma operação: '))
    if r == 1:
        resultado = n1 + n2
        print('Você escolheu soma')
        sleep(1)
        print(f'O resultado de {n1} + {n2} é {resultado}')
    elif r == 2:
        resultado = n1 * n2
        print('Você escolheu miltiplicação')
        sleep(1)
        print(f'O resultado de {n1} x {n2} é {resultado}')
    elif r == 3:
        print('Você escolheu ordem numerica')
        if n1 >= n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}')
    elif r == 4:
        print('Informe os valores novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif r == 5:
        print('Finalizando....')
    else:
        r = int(input('Opção invalida escolha novamente'))
        print('-=-' * 30)



