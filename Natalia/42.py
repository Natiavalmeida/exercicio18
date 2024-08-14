#42 - usuário digitará dez numero
# O programa deverá calcular quantos deles são maiores que dez.
controle = 0
for i in range(0,10):
    entrada = input('Digite o número ')
    numero = int(entrada)
    #entrada = int(input('Digite um numero'))

    if numero > 10:
        controle+=1

print('Existem', controle, 'numero(s) maiores que 10')