programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Function"])

# adding a new item in the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# wiping a dictionary
# empty_dictionary = {}
# programming_dictionary = {}
# print(programming_dictionary)

# edit an item in the dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])