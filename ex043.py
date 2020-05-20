# CALCULO DE IMC

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (M) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é {:.1f} '.format(imc))

if imc < 18.5:
    print('Voce esta abaixo do peso NORMAL! ')
elif 18.5 <= imc < 25:
    print('PARABENS!!! voce esta no peso ideal ')
elif 25 <= imc < 30:
    print('Voce esta em SOBREPESO!')
elif 30 <= imc < 40:
    print('Voce m OBESIDADE!')

elif imc >= 40:
    print('Voce esta em OBESIDADE MORBIDA!!!')