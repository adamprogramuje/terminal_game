# Tic Tac Toe
import random

def main():    
    possibilities = ['123', '456', '789', '147', '258', '369', '159', '357']
    board = [1,2,3,4,5,6,7,8,9]
    print('Welcome to Tic Tac Toe')

    def game_question(question, answer1, answer2):
        while True:
            user_answer = input(question).lower()

            if user_answer == answer1 or user_answer == answer2:
                break
            else: 
                print('Please choice one more time.')
        return user_answer
    
    
    game_type = int(game_question('Please choice your game: 1-for 2 player game or 2-for computer play: ', '1', '2'))
    player_one = game_question('Player One. Please choice "X" or "O" to play: ', 'x', 'o')
    if player_one == 'x':
        player_two = 'o' 
    else: 
        player_two = 'x'


    print(player_one)
    print(player_two)
    def board_view():
        view = f'''
         {board[0]} | {board[1]} | {board[2]}
        -----------
         {board[3]} | {board[4]} | {board[5]}
        -----------
         {board[6]} | {board[7]} | {board[8]}
        '''
        print(view)

    def filing_board(player, field_number):
        board[int(field_number) - 1] = player.upper()

        for i in range (len(possibilities)):
            possibilities[i] = possibilities[i].replace(field_number, player)


    def check_win(player):
        check = player * 3
        for x in possibilities:
            if x == check:
                print(f"Win player {player}!")
                return True

    def choice_player():
        while True:
            player = input('Player One. Please choice "X" or "O" to play: ')
    # player_one = input('Player One. Please choice "x" or "o" to play: ')
    # player_two = input('Player Two. Please choice "x" or "o" to play: ')

    while True:
        board_view()
        field = input('Choice your field Player One: ')
        filing_board(player_one, field)
        if check_win(player_one):
            break

        board_view()
        field = input('Choice your field Player Two: ')
        filing_board(player_two, field)
        if check_win(player_two):
            break

main()
        