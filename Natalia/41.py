#Construa uma página/programa onde o usuário digitará oito números, o programa
#escreverá na tela qual deles é o maior e qual deles é o menor.

lista = []

for i in range(8):
    numero = int(input('Digite o número: '))
    lista.append(numero)
    
    maior = max(lista)
    menor = min(lista)

print('O maior e ' + str(maior))
print('O menor e ' + str(menor))
