player1=input('Player One: Rock,Paper or Scissors?')
player2=input('Player 2: Rock, Parer or Scissors?')
if player1==player2:
    print('Draw')

elif player1=='Rock' and player2=='Scissors':
    print('Player One wins!')

elif player1=='Scissors' and player2=='Paper':
    print('Player One wins!')

elif player1=='Paper' and player2=='Rock':
    print('Player One wins!')

elif player2=='Rock' and player1=='Scissors':
    print('Player Two wins!')

elif player2=='Scissors' and player1=='Paper':
    print('Player Two wins!')

elif player2=='Paper' and player1=='Rock':
    print('Player Two wins!')
