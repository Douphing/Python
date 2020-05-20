A = int(input('Digite o primeiro Valor: '))
B = int(input('Digite o segundo valor: '))
C = int(input('Digite o segundo Valor: '))
menor = A
if B < A and B < C:
    menor = B
if C < A and C < B:
    menor = C
maior = A
if B > A and B > C:
    maior = B
    if C > A and C > B:
        maior = C

print('O menor valor digitado foi {}'.format(menor))
print('O maoir numero Digitado foi {}'.format(maior))

