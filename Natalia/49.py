#Construa uma página onde o usuário digitará o nome e a média de cinco alunos e o
#programa só aceitará a média do aluno caso ela esteja entre zero e dez.

alunos = []

for i in range (5):
    nome = input('Digite o nome do aluno: ')
    nota = float(input('Digite a media: '))

    while nota < 0 or nota > 10:
        print('Nota digitada errada')
        nota = float(input('Digite a media do aluno'))

alunos.append([nome, nota])

print(alunos)