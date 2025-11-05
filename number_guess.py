

import random

def play_game():
    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0
    low = 1
    high = 100

    print("Welcome to the Number Guessing Game!")
    
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    if difficulty == "easy":
        max_attempts = 10
    elif difficulty == "medium":
        max_attempts = 7
    else:
        max_attempts = 5

    while attempts < max_attempts:
        try:
            guess = int(input(f"Guess a number between {low} and {high}: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
            low = max(low, guess + 1)
        elif guess > secret_number:
            print("Too high! Try again.")
            high = min(high, guess - 1)
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}.")

# Main loop
while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! Goodbye!")
        break

 

            