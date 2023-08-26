# Rock paper scissors

import random

# Possible answer options
possibilities = ('rock', 'paper', 'scissors')
print('Welcome to rock paper scissors game.')



while True:
    human_choice = input("\nrock, paper, scissors (q to quit). Write your choice: ")
    if not human_choice in ('rock', 'paper', 'scissors', 'q'):
        print('Wrong answer!')
        continue

    # Assigning a random response for the computer
    computer_choice = random.choice(possibilities)

    if human_choice == 'q':
        break
    if computer_choice == human_choice:
        print(f'The computer chose: {computer_choice}. Result: remis')
    elif computer_choice == 'rock' and human_choice == 'paper':
        print(f'The computer chose: {computer_choice}. Result: You win')
    elif computer_choice == 'paper' and human_choice == 'scissors':
        print(f'The computer chose: {computer_choice}. Result: You win')
    elif computer_choice == 'scissors' and human_choice == 'rock':
        print(f'The computer chose: {computer_choice}. Result: You win')
    else:
        print(f'The computer chose: {computer_choice}. Result: You lose')