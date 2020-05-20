#GERENCIADOR DE PAGAMENTO

print('{:=^40}' .format(' Gerenciador de Pagamentos '))
preco = float(input('Preco das Compras : R$ '))
print('''FORMAS DE PAGAMENTO
[1] a vista  dinheiro/cheque
[2] a vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual a forma de pagamento? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra sera parcelada em 2x  de R$ {:.2f} sem JUROS '.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas vezes deseja parcelar? '))
    parcela = total / totparc
    print('Sua compra sera parcelada em {}x de {:.2f} com JUROS'.format(totparc, parcela))


    print('Sua compra de R$ {:.2f} vai custar R${:.2f} no final '.format(preco, total))