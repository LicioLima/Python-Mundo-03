palavras = ('aprender', 'correr', 'varrer', 'aprender', 'surfar',
            'programar', 'praticar', 'estudar', 'lutar', 'trabalhar',
            'progresso', 'crescer', 'ganhar', 'bonus', 'luta')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')