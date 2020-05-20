soma = 0
cont = 0
total = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont = cont + 1
        soma = soma + n
    total = total + 1

print('A soma de todos os {} Valores  é {} no total de {} numeros ipares '.format(cont, soma, total))