km = float(input('Quantos quilometros o carro percorreu? '))
dias = int(input('Quantos dias o carro foi alugado? '))
pago = (km * 0.15) + (dias * 60)
print('A quantidade a ser pago por km rodado e diarias sera o valor de R$ {:.2f}'.format(pago))