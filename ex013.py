salario = float(input('Qual é o salario do funcionario R$ '))
reajuste = salario + (salario * 15 / 100)
print('O salario do funcionario é R$ {:.2f} e com o reajuste de 15% sera R$ {:.2f}'.format(salario, reajuste))