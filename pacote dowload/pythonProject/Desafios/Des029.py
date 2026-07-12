v = int(input('Qual era a velocidade do veiculo: '))
if v > 80:
    multa = (v-80) * 7
    print(f'Você foi multado em R${multa}')
else:
    print('Você estava dentro da volocidade permitida')