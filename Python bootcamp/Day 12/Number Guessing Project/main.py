import art
import random

print(art.logo)

actual_number = random.randint(1,100)

print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose your difficulty level. Type 'easy' or 'hard': ").lower()

def guessing_game():
    correct_guess = False

    while correct_guess == False:
        attempt_hard = 6
        attempt_easy = 11
        if difficulty_level == "easy":
            while attempt_easy !=1:
                attempt_easy -=1
                print(f"You have {attempt_easy} attempts remaining to guess the number.")
                guess_number = float(input("Make a guess: "))
                if attempt_easy == 1 and guess_number != actual_number:
                    print("Sorry, you've ran out of guesses.")
                elif guess_number > actual_number:
                    print("Too high.")
                elif guess_number < actual_number:
                    print("Too low.")
                elif guess_number == actual_number:
                    print(f"You've guessed correctly!! The number is {actual_number} (:")
                    correct_guess = True
                    attempt_easy = 1
            break

        if difficulty_level == "hard":
            while attempt_hard !=1:
                attempt_hard -=1
                print(f"You have {attempt_hard} attempts remaining to guess the number.")
                guess_number = float(input("Make a guess: "))
                if attempt_hard == 1 and guess_number != actual_number:
                    print("Sorry, you've ran out of guesses.")
                elif guess_number > actual_number:
                    print("Too high.")
                elif guess_number < actual_number:
                    print("Too low.")
                elif guess_number == actual_number:
                    print(f"You've guessed correctly!! The number is {actual_number} (:")
                    correct_guess = True
                    attempt_hard = 1
            break

guessing_game()

print("Refresh the game to start over :)")



