from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL','TESOURA')
computador = randint (0, 2)


#print('O computador escolheu {} '.format(itens[computador]))
print('''Suas Opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))
print('JO', end='')
sleep(1)
print('KEN', end='')
sleep(1)
print('PO!!!')
sleep(2)
print('=' * 30)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou  {} '.format(itens[jogador]))

print('=' * 30)

if computador == 0:#PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1: #PAPEL
        print('JOGADOR VENCEU')
    elif jogador == 2:#TESOURA
        print('COMPUTADOR VENCEU')
    else:
        print('Jogada INVALIDA!')

elif computador == 1: #PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1: #PAPEL
        print('EMPATE')
    elif jogador == 2: #TESOURA
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVALIDA')

elif computador == 2: #TESOURA
    if jogador == 0: #PEDRA
        print('JOGADOR VENCEU')
    elif jogador == 1: #PAPEL
        print('COMPUTADOR VENCEU')
    elif jogador == 2: #TESOURA
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
