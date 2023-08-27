#-----------------------------------------------------
# Title: berryhill_calculator.py
# Author: Nolan Berryhill
# Date: 27 August 2023
# Description: Exercise 3.3 
#-----------------------------------------------------


# Define the addition function
def add(num1, num2):
    return num1 + num2 

# Define the subtraction function
def subtract(num3, num4):
    return num3 - num4

#-----------------------------------------------------
# Title: berryhill-calculator.py
# Author: Nolan Berryhill
# Date: 27 August 2023
# Description: Exercise 3.3 
#-----------------------------------------------------

# Define the division function
def divide(num5, num6):
    if num6 == 0:
        return "Cannot divide by zero"
    return num5 / num6

# Define the multiplication function
def multiply(num7, num8):
    return num7 * num8

# Variable for equations
num1 = 4
num2 = 4
num3 = 10
num4 = 6
num5 = 8
num6 = 2
num7 = 10
num8 = 2

# Calculate results
add_result = add(num1, num2)
subtract_result = subtract(num3, num4)
divide_result = divide(num5, num6)
multiply_result = multiply(num7, num8)

# Build strings for the results
add_str = f"{num1} + {num2} is {add_result}"
subtract_str = f"{num3} - {num4} is {subtract_result}"
divide_str = f"{num5} / {num6} is {divide_result}"
multiply_str = f"{num7} * {num8} is {multiply_result}"

# Print the output
print(add_str)
print(subtract_str)
print(divide_str)
print(multiply_str)


