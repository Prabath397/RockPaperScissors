# Rock-Paper-Scissors Game with Final Results
import random

options = ["rock", "paper", "scissors"]

print("✊✋✌ Welcome to Rock-Paper-Scissors Game!")

# Score tracking
player_wins = 0
computer_wins = 0
ties = 0
rounds = 0

while True:
    player = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()

    if player == "quit":
        print("\n📊 Final Results:")
        print(f"Total rounds played: {rounds}")
        print(f"Player wins: {player_wins}")
        print(f"Computer wins: {computer_wins}")
        print(f"Ties: {ties}")

        if player_wins > computer_wins:
            print("🏆 You are the final winner!")
        elif computer_wins > player_wins:
            print("💻 Computer is the final winner!")
        else:
            print("🤝 It's a tie overall!")
        print("Thanks for playing! 👋")
        break

    if player not in options:
        print("❌ Invalid choice! Please try again.")
        continue

    computer = random.choice(options)
    print(f"Computer chose: {computer}")
    rounds += 1

    if player == computer:
        print("It's a tie! 🤝")
        ties += 1
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win! 🎉")
        player_wins += 1
    else:
        print("Computer wins! 💻")
        computer_wins += 1
