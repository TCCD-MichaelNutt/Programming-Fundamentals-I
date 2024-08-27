import random

# Initializes the random number between 1 and 100
random_number = random.random(1, 100)

# Sets guess to -1
guess = -1

# Continues the game until the correct answer is given
while guess is not random_number:
    guess = input("Enter your guess: ")

    if guess > 0:
        print("Your number is too big!")
    elif guess < 0:
        print("Your number is too small!")
    else:
        print("You are correct!")
