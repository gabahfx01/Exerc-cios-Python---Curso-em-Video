from random import choice
a1 = str(input('Nome do primeiro aluno: '))
a2 = str(input('Nome do segundo aluno: '))
a3 = str(input('Nome do terceiro aluno: '))
a4 = str(input('Nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
sorteio = choice(lista)
print(f'O aluno sorteado foi {sorteio}')
