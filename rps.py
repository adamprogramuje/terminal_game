# Rock paper scissors
import random

possibilities = ('rock', 'paper', 'scissors')

while True:
    human_choice = input("rock, paper, scissors (q to quit). Write your choice: ")
    computer_choice = random.choice(possibilities)
    print(computer_choice)
    if human_choice == 'q':
        break
    if computer_choice == human_choice:
        print('remis')
    elif computer_choice == 'rock' and human_choice == 'paper':
        print('You win')
    elif computer_choice == 'paper' and human_choice == 'scissors':
        print('You win')
    elif computer_choice == 'scissors' and human_choice == 'rock':
        print('You win')
    else:
        print('You lose')