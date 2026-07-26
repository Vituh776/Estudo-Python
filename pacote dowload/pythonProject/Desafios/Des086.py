#matriz = [[], [], []]
matriz1 = []
matriz2 = []
matriz3 = []
numero = 0
for c in range (0, 3):
    numero = int(input(f'Digite um valor para [0, {c}]: '))
    matriz1.append(numero)
for c in range (0, 3):
    numero = int(input(f'Digite um valor para [1, {c}]: '))
    matriz2.append(numero)
for c in range (0, 3):
    numero = int(input(f'Digite um valor para [2, {c}]: '))
    matriz3.append(numero)
print('-=-' * 30)
print(f'[ {matriz1[0]} ] [ {matriz1[1]} ] [ {matriz1[2]} ]')
print(f'[ {matriz2[0]} ] [ {matriz2[1]} ] [ {matriz2[2]} ]')
print(f'[ {matriz3[0]} ] [ {matriz3[1]} ] [ {matriz3[2]} ]')
