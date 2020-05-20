velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade == 80:
    print('CUIDADO! você esta no limite de velocidade')
if velocidade > 80:
    print('MULTADO POR EXCESSO DE VEOLOCIDADE; limite permitido  de 80km/h')
    multa = (velocidade - 80) * 7
    print('Voce deve pagar multa de  R$ {:.2f}'.format(multa))
print('Tenha um bom dia!')
