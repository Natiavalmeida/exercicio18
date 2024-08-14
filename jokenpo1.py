player1 = input('Digite: Pedra, Papel, Papel ou Tesoura\n')
player2 = input('Digite: Pedra, Papel, Papel ou Tesoura\n')

if player1 == 'Pedra':
    if player2 == 'Pedra':
        print('Empate')
    elif player2 == 'Papel':
        print('player 2 ganhou!')
    elif player2 == 'Tesoura':
        print('player 1 ganhou!')

elif player1 == 'Papel':
    if player2 == 'Pedra':
        print('player 1 ganhou!')
    elif player2 == 'Papel':
        print('Empate')
    elif player2 == 'Tesoura':
        print('player 2 ganhou!')

elif player1 == 'Tesoura':
    if player2 == 'Pedra':
        print('player 2 ganhou!')
    elif player2 == 'Papel':
        print('player 1 ganhou!')
    elif player2 == 'Tesoura':
        print('Empate')
else:
    print('jogada invalida')
