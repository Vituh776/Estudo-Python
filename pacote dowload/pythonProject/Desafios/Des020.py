import random
a1 = str(input('Primeiro: '))
a2 = str(input('Segundo: '))
a3 = str(input('Terceiro: '))
a4 = str(input('Quarto: '))
alunos = [a1, a2, a3, a4]
random.shuffle(alunos)
print(f'A ordem de a apresentação vai ser {alunos}')