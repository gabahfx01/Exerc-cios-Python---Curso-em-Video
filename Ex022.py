#manipulando string
nome = str(input('Digite seu nome completo: '))
semesp = nome.replace(' ', '')
caract = len(semesp)
div = nome.split()
prin = len(div[0])
print(f'Maiusculo: {nome.upper()}\nMinusculo: {nome.lower()}\nCaracteres: {caract}\nCaracteres primeiro nome {div[0]}: {prin}')
