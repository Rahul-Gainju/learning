import random

def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ")
    option = ["rock", "paper", "scissor"]
    if player_choice not in option:
        print("Invalid choice. please choose rock, paper, or scissor.")
        return get_choices()
    computer_choice = random.choice(option)
    response = {"player_choice": player_choice, "computer_choice": computer_choice}
    return response

def check_winner(player, computer):
    print(f"You chose: {player}, computer chose: {computer}")
    # print("You chose" + player + ", computer chose " + computer)
    if player == computer:
        return("Its a tie")
    elif player =="rock":
        if computer == "scissor":
            return("Rock Smashes scissor! You win!")
        else:
            return "Paper covers rock! You lose."
    elif player =="paper":
        if computer == "rock":
            return("Paper covers rock! You win")
        else:
            return "scissor cuts paper! You lose."
    elif player =="scissor":
        if computer == "paper":
            return("Scissor cuts paper! You win")
        else:
            return "Rock smashes scissor! You lose."
        
response = get_choices()
result = check_winner(response["player_choice"], response["computer_choice"])
print(result)