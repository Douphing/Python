
# soma dos Pares

soma = 0
cont = 0
for n in range(1, 7):
    print('O valor da pocisao {}º '.format(n))

    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('voce informou  {} numeros PARES e a soma foi {}'.format(cont, soma))
