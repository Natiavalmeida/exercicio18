# Crie um jogo de par ou ímpar onde o computador irá gerar um número aleatório e o
# para resolver o jogo. Se a soma dos números for par, o usuário vence. Se for ímpar, o computador vence.

import random

def parImpar(a, b):
    soma = a + b
    if soma % 2 == 0:
        print('Voce Venceu')
    else:
        print('Computador Venceu')


a = int(input("Digite um número: "))

b = random.randint(0, 10)

print(f'Número aleatório gerado: {b}')

parImpar(a, b)
