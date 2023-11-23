from random import randint
from time import sleep
print('Vou pensar em um número de 0 a 10. Tente advinhar!')
numero = randint(1, 10)
escolha = int(input('Qual número eu escolhi? '))
print('PROCESSANDO em 3, 2, 1...')
sleep(2)
if escolha == numero:
    print(f'PARABENS, pensamos iguais no número {numero}')
else:
    print(f'Poxa você errou, eu escolhi o número {numero}')
