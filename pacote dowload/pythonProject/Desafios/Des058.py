import random
from time import sleep
computador = random.randint(0,10)
contador = 1
print('-=-' * 30)
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
print('-=-' * 30)
chute = int(input('Em q numero eu pensei? '))
print('Processando.....')
sleep(3)
if computador == chute:
    print('Parabens você acertou de primeira')
else:
    while computador != chute:
        chute = int(input('Errou tente novamente: '))
        contador = contador + 1
    print('Finalmente acertouKKKK')
print(f'O numero sorteado era {computador}')
print(f'Quantidade de chutes necessarios: {contador}')