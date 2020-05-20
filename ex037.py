#Programa de BASE DE CONVERSOES

num = int(input('Digite um Numero Inteiro: '))
print('''Escolha uma das bases para convercoes: 
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Sua Opcao: '))
if opcao == 1:
    print('{} convertido para Binario é igual  a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('OPCAO INVALIDA, tente Novamente!!!')