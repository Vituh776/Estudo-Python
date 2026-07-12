num = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dessezete', 'Dezoito', 'Dezenove', 'Vinte')
n = 0
while n != len(num):
    n = int(input('Escolha um numero de 0 a 20: '))
    print(num[n])
