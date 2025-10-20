import art


def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions -- subtract, multiply and divide.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values.
# keys = "+", "-", "*" and "/"

math_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# print(math_dictionary)

# TODO: Use the dictionary operations to perform the calculations.
# multiply 4*8 using the dictionary
# print(math_dictionary["*"](4, 8))

import art
print(art.logo)

def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in math_dictionary:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the second number?: "))
        answer = math_dictionary[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()
