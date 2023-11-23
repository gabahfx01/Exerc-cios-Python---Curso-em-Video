sal = float(input('Digite seu salario atual: '))
aum = float(input('De quantos % foi o aumento? '))
nsal = sal + (aum / 100 * sal)
print(f'Seu salario de R${sal:.2f}, com {aum}% vai passar a ser R${nsal:.2f}')