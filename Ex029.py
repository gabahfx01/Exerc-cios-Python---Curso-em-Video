velocidade = float(input('Qual a velocidade do carro KM? '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Parabens, você está dirigindo com segurança!')
else:
    print(f'Calma la meu pequeno gafanhoto, tira o pe do acelerador um pouco ai!\nSua punição foi uma multa de R${multa:.2f}')