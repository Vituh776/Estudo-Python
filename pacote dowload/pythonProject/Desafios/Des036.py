print('\033[34m-=-' * 30)
print('Aprove seu empréstimo')
print('-=-' * 30 )
vc = float(input('\033[mQual o valor da casa? R$'))
s = float(input('Qual o seu salario? R$'))
a = int(input('Quantos anos você quer as parcelas? '))
vp = vc / (a * 12)
vp1 = (s / 100) * 30
if vp <= vp1 :
    print('\033[1;32mParabréns seu empretimo foi aprovado!!!\033[m')
else:
    print('\033[1;31minfelizmente o seu empréstimo não foi aprovado')
print(vp1)
print(vp)