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
        computer = 'o'
    else: 
        player_two = 'x'
        computer = 'x'


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

    def check_board():
        state = True
        for i in board:
            if type(i) == int:
                state = False
        if state == True:
            print('Draw!')
        return state    
        
    def check_win(player):
        check = player * 3
        for x in possibilities:
            if x == check:
                board_view()
                print(f"Win player {player}!")
                return True

    def user_field_choice(player_name):
        while True:
            try:
                field = int(input(f'Choice your field {player_name}: '))
            except ValueError:
                print('Wrong data!')
                continue
            
            if board[field - 1] == 'X' or board[field - 1] == 'O':
                print('The field is occupied!')
            else:
                break
        return str(field)
    
    def computer_player():
        choice = ''
        board_view()
        while type(choice) != int :
            choice = random.choice(board)
        filing_board(computer, str(choice))
        print('Computer choice: ', choice)
        if check_win(computer) or check_board():
            return True

        
    
    def game(name, player):
        board_view()
        field = user_field_choice(name)
        filing_board(player, field)
        if check_win(player) or check_board():
            return True
    
    def one_vs_one():
        while True:
            if game('Player One', player_one):
                break

            if game('Player Two', player_two):
                break

    def one_vs_computer():
        while True:
            if game('Player One', player_one):
                break

            if computer_player():
                break

    if game_type == 1:
        one_vs_one()
    elif game_type == 2:
        one_vs_computer()

main()
        