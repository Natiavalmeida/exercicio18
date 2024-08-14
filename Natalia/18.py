# 18 - Construa um jogo de pedra, papel e tesoura

player1 = input('Player1 Digite: Pedra, Papel, Papel ou Tesoura\n')
player2 = input('Player2 Digite: Pedra, Papel, Papel ou Tesoura\n')

if ((player1=='Pedra'and player2=='Tpapeesoura') or
    (player1=='Papel' and player2== 'Pedra') or
    (player1=='Tesoura' and player2== 'Papel')):
    print('player 1 ganhou!')
elif(player1 == player2):
    print('Empate')
else:
    print('player 2 ganhou!')