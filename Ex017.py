from math import hypot
cat1 = float(input('Qual é o cateto oposto: '))
cat2 = float(input('Qual é o cateto adjacente: '))
hyp = hypot(cat1, cat2)
print(f'A hypotenusa desses cateto é {hyp:.2f}')
