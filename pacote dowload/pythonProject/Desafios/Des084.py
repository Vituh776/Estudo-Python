galera = []
maispeso = menpeso = 0 
while True:
    pessoa = str(input('Nome: '))
    peso = float(input('Peso: '))
    galera.append([pessoa, peso])
    if len(galera) == 1:
        maispeso = menpeso = peso
    else:
        if peso > maispeso:
            maispeso = peso
        if peso < menpeso:
            menpeso = peso
    resp = str(input('Deseja continuar?[S/N] ')).strip()
    if resp in 'Nn':
        break
print(galera)
print(maispeso)
print(menpeso)
for i, p in enumerate (galera):
    if p == maispeso:
        print(f'O maior peso foi {galera[i:1]}')





'''print(f'O maior peso foi de {maispeso}. Peso de {galera}')
print(f'O menor peso foi de {menpeso}. Peso de {}')
print(galera)'''
