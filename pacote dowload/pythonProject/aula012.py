nome = str(input('Qual o seu nome? '))
if nome == 'Victor':
    print('\033[31mQue nome bonito!!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Amanda':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Que nome normal')
print(f'Tenha um bom dia, {nome}!')