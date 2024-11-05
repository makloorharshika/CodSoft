import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Main function to run the game
def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions: Enter 'rock', 'paper', or 'scissors' to play. Enter 'quit' to exit the game.")

    while True:
        # Get the user's choice
        user_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()
        
        if user_choice == "quit":
            print("Exiting the game. Thank you for playing!")
            break
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        # Get the computer's choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        # Display scores
        print(f"Score: You - {user_score} | Computer - {computer_score}")

        # Ask if the user wants to play again
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

# Run the main function
if __name__ == "__main__":
    main()
