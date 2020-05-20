salario = float(input('Qual é o salario do funcionario? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem recebe R${:.2f} passa a receber R${:.2f} agora'.format(salario, novo))