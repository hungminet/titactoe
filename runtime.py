from tictactoe import *
board = [[X, O, O],
         [EMPTY, X, X],
         [EMPTY, EMPTY, EMPTY]]
tupl = (2, 2)
print('Player:',player(board))
print('Best move:',minimax(board))
a=4
#print(result(board,tupl))