#Rock paper sissors game!
import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("Rock, paper or Scissors?: ").lower()

    if player==computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Result: Tie")

    elif player == "rock":
        if computer == "paper":
                print("Computer: ", computer)
                print("Player: ", player)
                print("Result: Computer won!")   
        if computer == "scissors":
                print("Computer: ", computer)
                print("Player: ", player)
                print("Result: Player won!")

    elif player == "paper":
        if computer == "rock":
                print("Computer: ", computer)
                print("Player: ", player)
                print("Result: Player won!")
        if computer == "scissors":
                print("Computer: ", computer)
                print("Player: ", player)
                print("Result: Computer won!")

    elif player == "scissors":
        if computer == "paper":
                print("Computer: ", computer)
                print("Player: ", player)
                print("Result: Player won!")
        if computer == "rock":
                print("Computer: ", computer)
                print("Player: ", player)
                print("Result: Computer won!")
                
    play_again = input("Want to play again (yes/no): ").lower()
    if play_again != "yes":
     break
print("Bye!")
