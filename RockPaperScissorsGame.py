import random

def get_choices():
    player_choice = input("Enter a choice(Rock, Paper, Scissor): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice,"computer" : computer_choice}
    return choices 

def check_win(player, computer):
    print (f"You chose {player}, Computer chose {computer}.")
    if player == computer:
        return "It's a Tie!"
    elif player == "rock": 
        if computer == "scissors" :
            return "Rock smashes the scissors! You Win!"
        else:
            return "Paper covers rock! You Lose!"
    elif player == "paper": 
        if computer == "rock" :
            return "Paper covers rock! You Win!"
        else:
            return "Scissors cuts the paper! You Lose!"
    elif player == "scissors": 
        if computer == "rock" :
            return "Rock smashes the scissors! You Lose!"
        else:
            return "Scissors cuts the paper! You Win!"    

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
    
