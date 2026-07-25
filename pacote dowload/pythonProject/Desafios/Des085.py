numeros = [[], []]
for c in range (1, 8):
    numero = int(input(f'Digite o {c}° valor: '))
    if numero % 2 == 0:
        numeros.insert(0, numero)
    else:
        numeros.insert(1, numeros)
print('-=-' * 30)
print(f'Esse foram os valores pares q você digiou {numeros[0]}')