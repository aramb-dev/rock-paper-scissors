import random as random

choice = ["rock", "paper", "scissors"]

def computer():
    global choice
    choice = ["rock", "paper", "scissors"]
    global computer_choice
    computer_choice = random.choice(choice)
    return computer_choice

def rock_paper_scissors():

    user_input = input("Enter a choice: (rock, paper, scissors): ")
    user_input = user_input.lower()
    if user_input not in choice:
        print("Invalid input")

    computer_input = computer()

    if computer_input == user_input:
        print("It's a tie!")

    if computer_input == "rock":
        if user_input == "paper":
            print("You lose!")
        elif user_input == "scissors":
            print("You win!")


    if computer_input == "paper":
        if user_input == "scissors":
            print("You lose!")
        elif user_input == "rock":
            print("You win!")
    if computer_input == "scissors":
        if user_input == "rock":
            print("You lose!")
        elif user_input == "paper":
            print("You win!")



still_playing = True

while still_playing:
    rock_paper_scissors()
    play_again = input("Play again? (y/n): ")
    def play_again_def():
        global play_again
        play_again = input("Play again? (y/n): ")
    if play_again == "n":
        still_playing = False
    elif play_again == "y":
        continue
    else:
        print("Invalid input")
        still_playing = False