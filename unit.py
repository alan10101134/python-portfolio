import random

global player_wins
global computer_wins
player_wins = 0
computer_wins = 0

def game():
    choices = ["rock", "paper", "scissors"]

    print("Welcome to rock paper scissors!")
    player_choice=input("What would you like to choose? Rock, Scissors, or Paper?")
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if player_choice == computer_choice:
            print("It's a tie!")
    elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "scissors" and computer_choice == "paper") or
            (player_choice == "paper" and computer_choice == "rock")
        ):
            print("You win this round!")
            
    else:
            print("Computer wins this round!")





game()
