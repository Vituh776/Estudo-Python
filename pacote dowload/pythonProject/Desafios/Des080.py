numeros = []
for c in range (0, 5):
    numero = int(input('Digite um numero: '))
    if numero >= max(numeros):
        numeros.append(numero)