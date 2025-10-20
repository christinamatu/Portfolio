## Nested if/else statements

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("How old are you?"))

if height >= 120:
    print("You can ride the rollercoaster :)")
    if age <= 12:
        print("Please pay $5")
    elif age <= 15:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride :(")



## if / elif / else
# if condition1:
#     do A
# elif condition2:
#    do B
# else:
#    do this
