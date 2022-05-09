expressão = str(input('Digite sua expressão: '))
pilha = []
for simb in expressão:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append()
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão NÃO é válida!')
