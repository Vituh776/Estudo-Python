import random
from time import sleep
computador = random.randint(0,5)
print('-=-' * 30)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 30)
chute = int(input('Em q numero eu pensei? '))
print('Processando.....')
sleep(3)
if computador == chute:
    print('Parabens você acertou')
else:
    print('Não foi dessa vez')
print(f'O numero sorteado era {computador}')