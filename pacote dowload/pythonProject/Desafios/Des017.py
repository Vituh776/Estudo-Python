from math import hypot
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
h = hypot(co, ca)
print(f'O comprimento da hipotenusa é {h:.2f}')