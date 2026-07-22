resposta = 'S'
numeros = []
while resposta == 'S':
    numero = int(input('Digite um valor: '))
    if numero in numeros:
        print('Valor duplicado! Não vou adicionar...')
    else:
        numeros.append(numero)
        print('Valor adicionado com sucesso!!!')
    resposta = input('Deseja continuar?[S/N] ').upper().strip()[0]
print('-=-' * 30)
print(f'Os valores digitados foram {numeros}')