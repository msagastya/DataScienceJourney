# guess.py
import random

secret_number = random.randint(1, 100)
guess = None
while guess != secret_number:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number.")