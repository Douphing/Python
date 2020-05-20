#prestação da casa e salario do comprador

casa = float(input('Valor da casa R$ '))
salario =  float(input('Salario do comprador da casa R$ '))
anos = int(input('Qauntos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 /100
print('Para pagar uma casa  de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' A prestacao  sera de R$ {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Credito Liberado!!!')
else:
    print('Credito NEGADO!!!')