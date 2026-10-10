import random
ar = input("Do you wanna play rock paper scissors? (yes/no): ")
if ar in ["yes","y"]:
    print("Great! Lets play.")
    # game logic
    def get_winner(player, computer):
        if player == computer:
            return "Draw"
        if (player == "rock" and computer == "scissors") or \
        (player == "scissors" and computer == "paper") or \
        (player == "paper" and computer == "rock"):
            return "You win!"
        return "Computer wins!"
    choices = ["rock","paper","scissors"]
    while True:
        player = input("Choose rock, paper or scissors: ").strip().lower()
        if player not in choices:
            print("Invalid choice!")
            continue
        computer = random.choice(choices)
        print("Computer chose:", computer)
        print(get_winner(player, computer))
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break
    print("Maybe next time!")
elif ar in ["no","n"]:
    print("Maybe next time!")
else:
    print("Invalid input!")