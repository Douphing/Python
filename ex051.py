# desenvolvendo um programa de progrecao aritimedica PA mostrando os 10 primeiros

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
'''decimo termo de uma progressao aritimedica / enerzimo termo da PA '''
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end='-> ')
print('Acabou')
