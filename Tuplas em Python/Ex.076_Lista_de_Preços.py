material = ('lápis', 1.25,
            'borracha', 0.70,
            'caderno', 17.90,
            'estojo', 5.19,
            'Transferidor', 4.20,
            'Compasso', 5.15,
            'Mochila', 50.75,
            'Canetas', 34.90,
            'Livro', 54.20)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^38}')
print('-' * 40)
for pos in range(0, len(material)):
    if pos % 2 == 0:
        print(f'{material[pos]:.<30}', end='')
    else:
        print(f'R${material[pos]:>7.2f}')
print('-' * 40)