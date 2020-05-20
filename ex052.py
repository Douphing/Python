# Numeros Primos divisivel 2 vezes por 1 e por ele mesmo

num = int(input('Digite um numemero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot +=1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end=' ')
print('\n\033[33m O numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('por isso o numero {} \033[m É  PRIMO!!!'.format(num))
else:
    print('O numero {} \033[m NÂO é PRIMO!!!'.format(num))

    