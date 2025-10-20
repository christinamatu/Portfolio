## first attempt without using hints and video guides

from random import randint

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import art

print(art.logo)
print("Let's play a game of Blackjack!")

def game():
    user1 = random.randint(2, 11)
    user2 = random.randint(2, 11)
    user_total = user1+user2

    computer1 = random.randint(2, 11)
    computer2 = random.randint(2, 11)
    computer_total = computer1+computer2

    print(f"User: [{user1}, {user2}]\nComputer: [{computer1}, {computer2}]")
    print(f"User total: {user_total}\nComputer total: {computer_total}")

    blackjack = True
    while blackjack:
        if user_total == 21:
            print("User wins! :)")
        elif user_total > 21:
            while user1 or user2 == 11:
                if user_total > 21 # need help with this portion of code
        elif computer_total == 21:
            print("Computer wins! Better luck next time")
        elif user_total == computer_total:
            print("Draw! Try again.")
        else:
            print("Computer wins! Better luck next time")

    more_cards = input("Do you want to take another card: yes or no?").lower
    if more_cards == "yes":
        user3 = random.randint(2, 11)
        user_total = user1 + user2 + user3
        print(f"User: [{user1}, {user2}, {user3}]")
    else:
        computer3 = random.randint(2, 11)
        computer_total = computer1 + computer2 + computer3
        print(f"Computer: [{computer1}, {computer2}, {computer3}]")

    if computer_total > 21:
        print(f"User wins! :)\nUser total: {user_total}, Computer total: {computer_total}")
    if user_total > computer_total:
        print(f"User wins! :)\nUser total: {user_total}, Computer total: {computer_total}")
    if user_total == computer_total:
        print("Draw! Try again.\nUser total: {user_total}, Computer total: {computer_total}")
    else:
        print("Computer wins! Better luck next time.\nUser total: {user_total}, Computer total: {computer_total}")



game()
