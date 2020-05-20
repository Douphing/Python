# Alistamento Militar
from datetime import  date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} idade em {} '.format(nasc, idade, atual))
if idade == 18:
    print('Voce precisa se alistar IMEDIATAMENTE!!! ')

elif idade < 18:
    saldo = 18 - idade
    print('Ainda Faltam {} anos para alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {} ano'.format(ano))


elif idade > 18:
    saldo = idade - 18
    print('Voce deveria ter se alistado ha {} anos '.format(saldo))
    ano = atual -saldo
    print('Seu alistamento foi  em {}'.format(ano))


