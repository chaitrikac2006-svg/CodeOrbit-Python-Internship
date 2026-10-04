# Number Guessing Game

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Count the number of attempts
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")

# Allow the user to keep guessing
while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number.")
            print("Number of attempts:", attempts)
            break

    except ValueError:
        print("Please enter a valid number.")
