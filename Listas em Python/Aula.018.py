Pessoas = list()
Etária = list()
totmai = totmen = 0
for i in range (0, 2):
    Etária.append(str(input('Nome: ')))
    Etária.append(int(input('Idade: ')))
    Pessoas.append(Etária[:])
    Etária.clear()

for r in Pessoas:
    if r[1] >= 21:
        print(f'{r[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{r[0]} é menor de idade')
        totmen += 1
print(f'A quantidade de maiores é {totmai} e a de menores é {totmen}')