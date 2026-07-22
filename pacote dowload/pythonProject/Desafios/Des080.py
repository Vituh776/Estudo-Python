numeros = []
for c in range (0, 5):
    numero = int(input('Digite um numero: '))
    if c == 0 or numero > numeros[-1]:
        numeros.append(0)
    else:
        pos = 0
        while pos < len(numeros):
            if numero <= numeros[pos]:
                numeros.insert(pos, numero)
                break
            pos += 1
print('-=-' * 30)
print(f'Os valores digitadis foram {numeros}')