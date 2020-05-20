preco = float(input('Qual é o preco do produto R$ '))
novo = preco - (preco * 5 / 100)
print('O preco do produto  custa R$ {:.2f} e com o disconto de 5% vai custar R$ {:.2f}'.format(preco, novo))