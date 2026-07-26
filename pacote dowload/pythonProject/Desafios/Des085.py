numeros = [[], []]
numero = 0
for c in range (1, 8):
    numero = int(input(f'Digite o {c}° valor: '))
    if numero % 2 == 0:
        numeros[0].insert(0, numero)
    else: 
        numeros[1].insert(1, numero)
numeros[0].sort()
numeros[1].sort()
print('-=-' * 30)
print(f'Todos os valores {numeros}')
print(f'Esses foram os valores pares que você digiou {numeros[0]}')
print(f'Esses foram os valores impares que você digitou {numeros[1]}')