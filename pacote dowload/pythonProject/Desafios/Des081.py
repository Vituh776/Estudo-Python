resposta = 'S'
numeros = []
while resposta == 'S':
    numeros.append(int(input('Digite um numero: ')))
    resposta = input('Deseja continuar?[S/N] ').upper().strip()[0]
print('-=-' * 30)
numeros.sort(reverse = True)
print(f'Você digitou {len(numeros)} elementos')
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista!!!')
else:
    print('O valor 5 não faz parte da lista!!!!!!')