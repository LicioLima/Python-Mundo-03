valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores decrescentes {valores} ')
if 5 in valores:
    print(f'O cinco está aqui')
else:
    print('Não tem 5 aqui!')