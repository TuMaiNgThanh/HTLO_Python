#1. The Coffee Shop Receipt (Input, Print, Operations)
#Scenario: You are writing the software for a coffee shop.
#Task:
#Create a variable price for a coffee (e.g., 5.00).
#use input() to ask the user "How many cups would you like?".
#Convert that input into an integer.
#Calculate the total (price * quantity).
#Use print() to show a message like: "Your total is $15.0".

coffee = 5.00
input = int(input("How many cups would you like? "))
total = coffee * input
print(f"Your total is ${total}")

#Task 2:
#Create an empty list called guests = [].
#Create a for loop that runs 3 times (using range(3)).
#Inside the loop, ask the user for a "Guest Name".
#Use .append() to add that name to your guests list.
#At the end (outside the loop), print the full list of guests.

guests = []
for i in range (3):
    name = input("Guest Name: ")
    guests.append(name)
print(guests)


#Task 3:
#Define a variable secret_code = "1234".
#Create a variable user_guess and set it to an empty string "".
#Create a while loop that runs as long as user_guess is not equal (!=) to secret_code.
#Inside the loop, use input() to update user_guess.
#After the loop finishes (meaning they got it right), print "Access Granted!".

secret_code = "1234"
user_guess = input('Enter the password: ')
while user_guess != secret_code:
    user_guess = input("Wrong password, try again: ")
print("Access Granted!")

# Task 4:
# Create a list with some items: cart = ["Apple", "Banana", "Milk"].
# Print "Checkout complete!".
# Use the .clear() method to empty the list.
# Print the cart again to confirm it is empty (it should show []).

cart = ["Apple", "Banana", "Milk"]
print("Checkout complete!")
cart.clear()
print(cart)

# Task 5:
# Define a function named calculate_yearly that takes one parameter: monthly_pay.
# Inside the function, multiply monthly_pay by 12 and store it in a variable called yearly.
# Print a message inside the function: "Total yearly salary is: [amount]".
# Call the function at the bottom of your code with a number, for example: calculate_yearly(3000).

def calculate_yearly(month_pay):
    yearly = month_pay * 12
    print(f"Total yearly salary is: {yearly}")
calculate_yearly(3000)

#Task 6
# Scenario: You want to buy a new laptop that costs $1000. You need a program that keeps asking you to deposit money until you have enough.
# Task:
# Create a variable current_savings = 0.
# Create a while loop that runs as long as current_savings < 1000.
# Inside the loop, ask input(): "Deposit amount: ".
# Convert the input to a float and add it to current_savings (use current_savings = current_savings + amount).
# Print the new current balance inside the loop.
# After the loop finishes, print "Goal reached! You have enough money."

current_savings = 0
while current_savings < 1000:
    amount = float(input("Deposit amount: "))
    current_savings += amount
    print(f"Current balance: ${current_savings}")
print("Goal reached! You have enough money.")

#Task 7
# Task:
# Start with an empty list: inventory = [].
# Create a list of incoming items manually: truck_items = ["Keyboard", "Mouse", "Monitor"].
# Create a for loop that goes through truck_items.
# Inside the loop, use .append() to move the item into your inventory list.
# Inside the loop, print "Added [item] to inventory".
# Finally, print the full inventory list.
inventory =[]
truck_items = ['keyboard', 'mouse', 'monitor']
for item in truck_items:
    inventory.append(item)
    print(f'Added {item} to inventory.')
print(inventory)

#Task 8
# Task:
# Create a list: history = ["google.com", "youtube.com", "facebook.com"].
# Print "Current history:", followed by the list.
# Simulate the user clicking delete by asking an input(): "Type 'DELETE' to clear history: ".
# (Optional challenge: Use an if statement to check if they typed "DELETE").
# Run history.clear().
# Print "History is now:", followed by the history variable (it should be empty).
history = ['google.com','youtube.com','facebook.com']
print("Current History:")
print(history)
delete_site = input("Enter the site you want to delete: ")
if delete_site in history:
    history.remove(delete_site)
    print(f"{delete_site} has been removed from your history.")
else:
    print(f"{delete_site} not found in your history.")
print("Updated History:")
print(history)  

# Task 9:
# Define a function called calc_area that accepts one parameter: width.
# Inside the function, do the math: area = width * width.
# Inside the function, use print() to show: "The area is [area] square meters".
# Call your function three times with different numbers (e.g., calc_area(5), calc_area(10), calc_area(12)).
def calc_area(width):
    area = width * width
    print(f"The area is {area} square meters")
calc_area(5)
calc_area(10)
calc_area(12)

# Task 10:
# Use input() to ask for "First Name".
# Use input() to ask for "Last Name".
# Use input() to ask for "Age".
# Create a formatted print statement using an f-string (put an f before the quotes) to say:
# "Welcome, {First Name} {Last Name}! You are {Age} years old."
# (You can use commas: print("Welcome", first_name, last_name...))
first_name = input("First Name: ")
last_name = input("Last Name: ")
age = input("Age: ")
print(f"Welcome, {first_name} {last_name}! You are {age} years old.")



# Task 11:
# Step-by-Step Instructions (Try to code this yourself first!)
# The Setup:
# Create an empty list called cart.
# Create a variable total_price and set it to 0.
# The Function (def):
# Define a function called show_menu().
# Inside the function, print 3 options:
# "1. Add Item"
# "2. Clear Cart"
# "3. Checkout (Exit)"
# The Loop (while):
# Start a while True: loop (this runs forever until we tell it to break).
# Inside the Loop:
# Call your show_menu() function.
# Create a variable choice that asks the user for input(): "Choose an option (1-3): ".
# The Logic (if/elif):
# Option 1 (Add):
# Ask for input: "Enter item name: ".
# Ask for input: "Enter price: " (Convert this to a float).
# Use .append() to add the name to your cart list.
# Use Math to add the price to total_price (e.g., total_price = total_price + price).
# Print "Item added!".
# Option 2 (Clear):
# Use .clear() on the cart list.
# Reset total_price to 0.
# Print "Cart is now empty."
# Option 3 (Checkout):
# Print "Receipt:" followed by the cart list.
# Print "Total to pay: $" followed by total_price.
# Use the break command to stop the loop.

cart = []
total_price = 0.0

def show_menu():
    print("1. Add Item")
    print("2. Clear Cart")
    print("3. Checkout (Exit)")

while True:
    show_menu()
    choice = input("Choose an option (1-3): ")
    
    if choice == '1':
        item_name = input("Enter item name: ")
        item_price = float(input("Enter price: "))
        cart.append(item_name)
        total_price += item_price
        print("Item added!")
        
    elif choice == '2':
        cart.clear()
        total_price = 0.0
        print("Cart is now empty.")
        
    elif choice == '3':
        print("Receipt:")
        print(cart)
        print(f"Total to pay: ${total_price}")
        break
        
    else:
        print("Invalid choice, please try again.")