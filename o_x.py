# Tic Tac Toe

possibilities = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]

board = [1,2,3,4,5,6,7,8,9]

board_view = f'''
 {board[0]} | {board[1]} | {board[2]}
-----------
 {board[3]} | {board[4]} | {board[5]}
-----------
 {board[6]} | {board[7]} | {board[8]}
'''

print(board_view)