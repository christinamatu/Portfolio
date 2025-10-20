## Loops with ranges

for number in range(1, 11, 3): #steps by 3
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)

## Coding exercise
for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)