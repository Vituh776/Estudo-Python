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
print(numeros)
print(numeros_pares)
print(numeros_impares)