from rich import print
from time import sleep
times = ('Palmeiras', 'Flamengo', 'Atlético', 'Cruzeiro', 'Fluminense', 'Botafogo', 'Mirassol', 'São Paulo', 'Bahia', 'Red Bull Bragantino', 'Athletico', 'Gremio', 'Internacional', 'Vasco', 'Vitória', 'Chapecoense', 'Santos', 'Corinthians', 'Coritiba', 'Remo')
print('-=-' * 15,  'Tabela Brasileirão 2026', '-=-' * 15)
sleep(2)
print('Primeiros Colocados.....')
sleep(1)
for i, nome in enumerate(times[:5], start=1):
    print(f'[bold green]{i}° {nome}')
    sleep(1)
print('-=-' * 15, 'Zona de Rebaixamento', '-=-' * 15)
for i, nome in enumerate(times[-4:], start=17):
    print(f'[bold red]{i}° {nome}')
    sleep(1)
print('-=-' * 30)
print(f'O time da Chapecoense está na posicão {times.index('Chapecoense')}° do Brasileirão')
print('-=-' * 30)
escolha = 'S'
while escolha == 'S':
    escolha = str(input('Você quer procurar outro time na tabela? [S/N] ')).strip().upper()[0]
    if escolha == 'S':
        procurar_time = str(input('Digite o time que quer procurar: ')).strip().capitalize()
        print(f'O time {procurar_time} está na posição {times.index(procurar_time)}°')
        print('-=-' * 30)
    else:
        break
print('Finalizando....')