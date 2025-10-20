from game_data import data
import random

# display art
import art
print(art.logo)

score = 0 #score keeping
game_should_continue = True
account_b = random.choice(data)

# format the account data into printable format
def format_data(account):
    """takes the account data and returns the printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

# use if statement to check is user is correct
def check_answer(user_guess, a_followers, b_followers):
    """take the user's guess and the follower counts and return if they got it right"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

while game_should_continue:
    # generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}.")
    print(art.vs)
    print(f"Against B: {format_data(account_b)}.")

    # ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # clear the screen
    print("\n" * 20)
    print(art.logo)

    # check if user is correct
    # get follower count of each account
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_account, b_follower_account)

    # give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You are right! :) Your current score is {score}. ")
    else:
        print(f"Sorry, that is wrong. Your final score is {score}. ")
        game_should_continue = False

    # score keeping

    # make the game repeatable

    # making account at position B become the next account at position A