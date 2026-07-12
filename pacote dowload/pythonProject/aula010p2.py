n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m >= 7:
    print('Parabens você passou de ano')
else:
    print('Infelizmente você não passou de ano')
print(f'Sua média foi {m}')