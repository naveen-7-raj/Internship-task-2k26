import random

print("🎮 Rock Paper Scissors Game")

# Score tracking
user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:
    # User input
    user_choice = input("\nEnter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    # Computer random choice
    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Game logic
    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("Result: You Win! 🎉")
        user_score += 1

    else:
        print("Result: Computer Wins! 🤖")
        computer_score += 1

    # Display scores
    print("\nScoreboard")
    print("You:", user_score)
    print("Computer:", computer_score)

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing! 👋")
        break