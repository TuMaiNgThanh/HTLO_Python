print("----------Ex_1----------")

name = input("Enter your name: ")
Birth_year = int(input("Enter your birth year: "))
current_year = 2026
print(f"welcome {name}, you are {current_year - Birth_year} years old.")

print("----------Ex_2----------")

n = int(input("Write a length of the rectangle: "))
m = int(input("Write a width of the rectangle: "))
area = n * m 
print(f"The area of the rectangle is: {area}")

print("----------Ex_3----------")

Age = int(input("Enter your age: "))
while Age < 0:
    print("Error age cannot be negative.")
    Age = int(input("Enter your age: "))
    for i in range(Age<0):
        print("Try again!")
if Age < 13:
    print("Child ticket: $5")
elif Age >= 13 and Age < 18:
    print("Teen ticket: $8")
else:
    print("Adult ticket: $12")

print("----------Ex_4----------")
number = int(input("Enter an integer number: "))
while number < 0:
    print("Invalid input. Please enter a non-negative integer.")
    number = int(input("Enter an integer number: "))

if number % 2 == 0:
    print(f"{number} is an even number.") 
else:
    print(f"{number} is an odd number.")

print("----------Ex_5----------")
number = int(input("Enter a integer: "))
for i in range (number):
    print(f"Multiplication Table with number {i}")
    for j in range (1,11):
        print(f"{i} x {j} = {i*j}")
print("End!")

print("----------Ex_6----------")

k = int(input("Enter a positiver interger k: "))
sum = 0
while k < 0:
    print("Invalid input. Please enter a positive integer.")
    k = int(input("Enter a positiver interger k: "))
for i in range (1,k+1):
    sum += i
print(f"The sum of the first {k} positive integers is: {sum}")

print("----------Ex_7----------")
country = input("Enter a capital city name in Vietnam: ")
while country != "Hanoi":
    print("Wrong! Try again.")
    country = input("Enter a capital city name in Vietnam: ")
    for i in range(country != "Hanoi"):
        print("Start with the letter H")
print("Correct! Hanoi is the capital city of Vietnam.")


print("----------Ex_8----------")
money =float(input("Enter an amount of money add to the account: "))
while money < 0:
    print("Invalid amount. Please enter a non-negative amount.")
    money = float(input("Enter an amount of money add to the account: "))
print (f"Total amount in the account: ${money:.2f}")


