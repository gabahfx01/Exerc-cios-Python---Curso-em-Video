from math import radians, cos, sin, tan
an = float(input('Digite um angulo: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print(f'O ângulo de {an} tem:\nSENO: {seno:.2f}\nCOSSENO: {cosseno:.2f}\nTANGENTE: {tangente:.2f}')
