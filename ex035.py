print(' -='*20)
print('Analisadior de TRIANGULO')
print(' -='*20)
r1 = float(input('Primeiro segmento '))
r2 = float(input('Segundo segmento '))
r3 = float(input('Terceirop segmanto '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(' O segmento pode formar Um triangulo ')
else:
    print('O segmento não pode formar Um triangulo ')