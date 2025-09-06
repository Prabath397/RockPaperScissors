# Rock-Paper-Scissors Game
import random

options = ["rock", "paper", "scissors"]

print("✊✋✌ Welcome to Rock-Paper-Scissors Game!")

while True:
    player = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()

    if player == "quit":
        print("Thanks for playing! 👋")
        break

    if player not in options:
        print("❌ Invalid choice! Please try again.")
        continue

    computer = random.choice(options)
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie! 🤝")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win! 🎉")
    else:
        print("Computer wins! 💻")
