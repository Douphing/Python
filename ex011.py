larg = float(input('a alrguara da parede é: '))
alt = float(input('a altura da parede é: '))
area = larg * alt
print('Sua parede tem dimensoes de {}x{} a area é {}m²'.format(larg, alt, area))
tinta = area / 2
print('para5 pintar essa parede voce precisa de {} litros de tinta'.format(tinta))