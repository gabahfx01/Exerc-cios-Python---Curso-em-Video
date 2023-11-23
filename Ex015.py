dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))
taxa = (dias * 60) + (km * 0.15)
print(f'O valor total a pagar é de R${taxa:.2f}')
