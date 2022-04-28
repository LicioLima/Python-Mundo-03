listaNum = []
mai = 0
men = 0
for i in range(0, 5):
    listaNum.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        mai = men = listaNum[i]
    else:
        if listaNum [i] > mai:
            mai = listaNum[i]
        if listaNum [i] < men:
            men = listaNum[i]
print('=-' * 30)
print(f'Você digitou os valores {listaNum}')
print(f'O maior valor digitado foi {mai}')
for i, v in enumerate(listaNum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men}')
for i, v in enumerate(listaNum):
    if v == men:
        print(f'{i}... ', end='')
print()