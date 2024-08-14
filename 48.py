# Construa uma página/programa onde o usuário digitará o nome e o bairro de dez
# pessoas. O programa exibirá o nome e bairro das pessoas em ordem alfabética.

cadastro = []

for i in range(0,3):
    aux = []
    nome = input('Digite seu nome: ')
    bairro = input('digite deu Bairro: ')

    aux = [nome, bairro]

    cadastro.append(aux)

cadastro.sort()
print(cadastro)