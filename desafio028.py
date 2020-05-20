from random import randint
from time import sleep
computador = randint(0, 5) # sorteio do computador
print('+ ' * 20)
print('Pense no Numero {}'.format(computador))
print('Vou Pensar em um numero entre 0 e 5. Tente adivinhar! ')
print('+' * 20)
jogador = int(input('Em qual Numero eu pensei? ')) # jogador adivinha
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabens! Você acertou!!! ')
else:
    print('Voce Perdeu, eu pensei no numero {} e não no numero {}. Tente outra vez! '.format(computador, jogador))
