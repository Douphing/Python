preco_do_produto = float(input('O produto em vitrine tem o valor de R$ '))
pgmto_vista = preco_do_produto - (preco_do_produto * 5 / 100)
pgmto_prcla  = preco_do_produto + (preco_do_produto * 10 / 100)
print('o valor do produto é R$ {:.2f},  a vista com desconto de 5% R$ {:.2f} e parcelado '
      'com acrecimo de 10%  R$ {:.2f}'.format(preco_do_produto, pgmto_vista, pgmto_prcla))