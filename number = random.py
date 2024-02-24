import random
import sys

def guess_game():
    number = random.randint(1, 100)
    guesses = 0

    print("Welcome to my random number guessing game")
    mes_1 = input("There is a number between 1 and 100. Do you wish to play? (yes/no): ")

    if "no" in mes_1.lower():
        sys.exit()

    if "yes" in mes_1.lower():
        guess = int(input("Good! Now, enter your guess (1 to 100): "))
        guesses += 1
    
    if guess == number:
        print("Congratulations! You guessed it right!")

    elif guess < number:
        print(f"Aww, try again! The number was {number}")

    else:
        print(f"Too bad! You guessed a bit too high. The number was {number}")
    
    mes_3 = input("Do you wish to replay the game? (yes/no): ")
    if "no" in mes_3.lower():
        sys.exit()

    if "yes" in mes_3.lower():
        guess_game()

guess_game()