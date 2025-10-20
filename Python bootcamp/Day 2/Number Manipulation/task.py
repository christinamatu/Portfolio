bmi = 84 / 1.65 ** 2

height = 1.65
weight = 84

# Calculate BMI using weight and height
BMI = weight/height**2
print(BMI)

# Flooring
print(int(BMI))

# Rounding the answer
print(round(BMI))

# Rounding to 2 decimal places
print(round(BMI, 2))

# Rounding to 3 decimal places
print(round(BMI, 3))

# ---------------
score = 0

# User scores a point (can be +, -, * or /)
score +=1
print(score)

# f-strings. You can use f-strings even inside of "" quotation marks
print("Your score is " + str(score))

score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}.")

