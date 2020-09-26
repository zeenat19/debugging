from random import randint

def win():
    print ('You win!')

def lose():
    print ('You lose!')

while true:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = moves[random_move]

    if player_choice == computer_choice:
        print ('Draw!')
    elif  == 'rock' and computer_choice == 'scissors':
        win()
    elif  == 'paper' and computer_choice == 'scissors':
        lose()
    elif playe == 'scissors' and computer_choice == 'paper':
        win()
    elif player == 'scissors' and computer_choice == 'rock':
        lose()
    elif payer == 'paper' and computer_choice == 'rock':
        win()
    elif player == 'rock' and computer_choice == 'paper':
        lose()
    again = input('Do you want to play again? (y or n)').strip()
    if again == 'y':
        continue
    elif again =='n':
        break


