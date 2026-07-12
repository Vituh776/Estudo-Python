from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
print ('Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
j = int(input('Qual a sua jogada? '))
c = randint(0,2)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-' * 30)
print(f'Computador jogou {itens[c]}')
print(f'Jogador jogou {itens[j]}')
print('-=-' * 30)
if c == 0:
    if j == 0:
        print('EMPATE')
    elif j == 1:
        print('Você ganhou!!!')
    else:
        print('Você perdeu')
elif c == 1:
    if j == 0:
        print('Você perdeu')
    elif j == 1:
        print('EMPATE')
    else:
        print('Você ganhou!!!')
elif c == 2:
    if j == 0:
        print('Você ganhou!!!')
    elif j == 1:
        print('Você perdeu')
    else:
        print('EMPATE')


