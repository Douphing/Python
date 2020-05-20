# Grupo de Idades de Maior idade
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 5):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
        print('Essa pessoa é maior ')
    else:
        totmenor += 1
        print('Essa pessoa é menor ')
print(' Temos {} pessoas maior de idade'.format(totmaior))
print(' Temos {} pessoas menor de idade'.format(totmenor))
