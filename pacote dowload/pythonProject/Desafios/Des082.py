numeros = []
numeros_pares = []
numeros_impares = []
resposta = 'S'
while resposta == 'S':
    numero = int(input('Digite um valor: '))
    numeros.append(numero)
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
    resposta = input('Deseja continuar?[S/N] ').upper().strip()[0]
print('-=-' * 30)
print(f'Esses são os numeros q vc digitou: {", ".join(map(str, numeros))}')
print(f'Esses são os numeros pares q vc digitou: {", ".join(map(str, numeros_pares))}')
print(f'Esses são os numeros impares q vc digitou: {", ".join(map(str, numeros_impares))}')