d = int(input('Quantos km: '))
if d <= 200:
    cal = d * 0.50
    print(f'O valor da sua passagem ficou R${cal}')
else:
    cal = d * 0.45
    print(f'O valor da sua passagem ficou R${cal}')
