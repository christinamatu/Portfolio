import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("Let's play a game of rock, paper, scissors! Type 0 for rock, 1 for paper and 2 for scissors. "))
# 0, 1, 2

print("You chose:")
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("The computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. Please try again.")
elif user_choice == 0 and computer_choice == 1:
    print("Sorry, you lost! :(")
elif user_choice == 0 and computer_choice == 2:
    print("You win! :D")
elif user_choice == 1 and computer_choice == 0:
    print("You win! :D")
elif user_choice == 1 and computer_choice == 2:
    print("Sorry, you lost! :(")
elif user_choice == 2 and computer_choice == 0:
    print("Sorry, you lost! :(")
elif user_choice == 2 and computer_choice == 1:
    print("You win! :D")
elif computer_choice == user_choice:
    print("It's a draw!")
