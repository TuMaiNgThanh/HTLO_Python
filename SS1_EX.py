# #Exercise 1: The Greeting
# Task: Write a program that asks the user for their name. Then, print a greeting message.
# Example:
# Input: Anh
# Output: Hello, Anh! Welcome to Python 

name =input("What's your name?: ")
print("Hello, " + name + "! Welcome to Python")
print(f"Hello, {name}! Welcome to Python")

# #Exercise 2: Simple Calculator
# Task: Ask the user to input two integer numbers (Number A and Number B). Calculate their sum (+) and print the result.
# Hint: Remember to convert the input to integer using int().
# Example:
# Input A: 10
# Input B: 5
# Output: The sum is: 15
A =int(input("The firts A number: "))
B =int(input("The second B number: "))
print(f"The sum is: {A + B}")

# #Exercise 3: Your Favorite Color
# Task: Create a variable called color and use input() to ask: "What is your favorite color?". Then print a sentence using that variable.
# Output format: Wow, [color] is a beautiful color!

Color =input("What's your favorite color?: ")
print(f"Wow, {Color} is a beautiful color!")
print("Wow, " + Color + " is a beautiful color!")

# #Exercise 4: Age Calculator
# Task: Ask the user for their Year of Birth. Calculate their current age (assuming the current year is 2026) and print it.
# Formula: Age = 2026 - Year of Birth
YOB =int(input("What is your Year of Birth?: "))
age = 2026 - int(YOB)
print (f"You are {age} years old this year.")

# Exercise 5: Basic Conversion
# Task: Ask the user to input an integer number. Print the binary representation of that number using the bin() function.
# Example:
# Input: 10
# Output: 0b1010

x =int(input("Input your integers number: "))
print(f"Your binary number is: {bin(x)}")

