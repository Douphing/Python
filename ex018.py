import math
angulo = float(input('Digite um angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
print('O  angulo de {} tem o Seno de {:.2f} '.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print(' O angulo de {} tem cosseno de {:.2f} '.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print(' O angulo de {} tem uma tangente de {:.2f} '.format(angulo, tangente))