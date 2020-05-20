distancia = float(input('Qual é a distancia da sua Viagem? '))
print('Voce  iniciara  uma viagem de {}km'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

'''preco = distancia *0.50
if distancia <=200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45'''


print('Sua viagem vai custar R${:.2f}'.format(preco))