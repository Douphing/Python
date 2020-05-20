# detector de Palindromo  invertendo palavras

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #split tratamento de texto
junto = ''.join(palavras)# juntas as palavras sem espacos

inverso = junto[::-1] # versao de fatiamento sem "for"
'''inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''

print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase não é um palindromo')
