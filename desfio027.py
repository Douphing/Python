n = str(input(' Digite seu Nome Completo: ')).strip()
nome = n.split()
print('Muito Prazer {} !'.format(n))
print(('Seu primeiro Nome é : {} '.format(nome[0])))
print('Seu ultimo nome é: {} '.format(nome[len(nome)-1]))

