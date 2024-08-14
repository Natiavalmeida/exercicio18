#Construa uma página/programa onde o usuário digitará três números e o programa
#exibirá, na tela, o maior entre eles.

numero1 = int(input('Digite o primeiro número> '))
numero2 = int(input('Digite o segundo número> '))
numero3 = int(input('Digite o terceiro número> '))

if numero1 >= numero2 and numero1 >= numero3:
    print ('o numero maior é: ', numero1)
elif numero2 >= numero3 and numero2 >= numero1:
    print  ('o numero maior é: ', numero2)
else: 
    print  ('o numero maior é: ', numero3)