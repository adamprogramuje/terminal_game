# Tic Tac Toe

#possibilities = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]
possibilities = ['123', '456', '789', '147', '258', '369', '159', '357']

board = [1,2,3,4,5,6,7,8,9]

def borad_view():
    view = f'''
     {board[0]} | {board[1]} | {board[2]}
    -----------
     {board[3]} | {board[4]} | {board[5]}
    -----------
     {board[6]} | {board[7]} | {board[8]}
    '''
    print(view)

borad_view()
def filing_board(player, field_number):
    board[int(field_number) - 1] = player
    print(board[int(field_number) - 1])
    for i in range (len(possibilities)):
        possibilities[i] = possibilities[i].replace(field_number, player)


def check_win(player):
    check = player * 3
    for x in possibilities:
        if x == check:
            print(f"Win player {player}!")

check_win('x')