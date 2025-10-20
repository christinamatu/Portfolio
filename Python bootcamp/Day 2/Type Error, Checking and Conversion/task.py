#len returns the length or number of words, len cannot take an integer

len("Hello")

print(len("Hello"))

print(type("Hello"))
print(type("123"))
print(type(123))
print(type(True))
print(type(0.123))

# Turning strings into integers
print(int("123") + int("456"))
# this only works if the string is a number and not words

# Can convert into
int()
float()
str()
bool()

print(str("Number of letters in your name: ") + str(len(input("Enter your name"))))
