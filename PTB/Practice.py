#Input and Print
#Print with mean you want to print something on the screen
#Input with mean you want to get some information from user
print("----------Ex_1----------")
#The Barista: Write a program that asks the customer for their name and their
#coffee order. Then, print a message like: "One large Latte for Sarah coming
#right up!"
print('Hey, welcome to the Coffee Shop!')
print('The Barista: What would you like to order?')
x = input('I would like to order a ')
print('The Barista: What your name is?')
name = input('My name is ')
print(f'The Barista: One {x} for {name} coming right up!')

print("----------Ex_2----------")
# ID Card Generator: Ask the user to input their First Name, Last Name, and
# Job Title. Print them out on separate lines, formatted like a digital badge
first = input("First Name: ")
last = input("Last Name: ")
job = input("Job Title: ")

print("----------------")
print(f"Name: {first} {last}")
print(f"Role: {job}")
print("----------------")

print("----------Ex_3----------")
# Tip Calculator: Create a program that asks the user for the total bill
# amount and then calculates a 15% tip on that amount. Print out the tip
bill = float(input("Enter bill amount: ")) # Convert text to decimal number

tip = bill * 0.15

print(f"A 15% tip would be: ${tip}")

#IF ELIF ELSE 
#If mean if something is true do this
#Elif mean else if something else is true do this
#Else mean if nothing is true do this

print('If Elif Else Statements')
print("----------Ex_1----------")
# Movie Ticket Kiosk: Ask the user for their age.
# ○ If age is under 12, print "Ticket price: $5".
# ○ If age is between 12 and 60, print "Ticket price: $12".
# ○ If age is over 60, print "Ticket price: $8".

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

print("----------Ex_2----------")
Q = input('Is it ranning today?') #yes/no
if Q== 'yes':
    print("Take an umbrella!")
else:
    A = input('Is it sunny today?') #yes/no
    if A== 'yes':
        print("Wear a sunglasses!")
    else:
        print("Have a cloudy day!")

print("----------Ex_3----------")
Q = input("What the color for a light?") #red/yellow/green
if Q == 'red':
    print("Stop!")
elif Q == 'yellow':
    print("Slow down!")
elif Q == 'green':
    print("Go!")
else:
    print("Invalid color!")


# for loop
# Loop through a block of code a number of times 
print("----------Ex_1----------")
seconds = int(input("Enter seconds: "))
for i in range(seconds, 0, -1):
    print(i)

print("Beep! Food is ready.")

print("----------Ex_2----------")
for i in range(1, 11): # 1 to 10
    print(f"Doing pushup number {i}")

print("All done with pushups!")
print("----------Ex_3----------")
number = int(input("Enter a number: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

#while loop
#while mean while something is true do this

print("----------Ex_1----------")
secret_password = "python"
user_input = input("Enter password: ")

while user_input != secret_password:
    print("Access Denied.")
    user_input = input("Try again: ") # Update variable inside loop

print("Welcome!")

print("----------Ex_2----------")
Battery = 0
while Battery < 100:
    Battery += 10
    print(f"Battery at {Battery}%")
print("Battery fully charged!")
print("----------Ex_3----------")
saving = 0
goal = 1000

while saving < goal:
    deposit = float(input("Deposit amount: "))
    saving = saving + deposit
    print(f"Current savings: ${saving}")

print("Goal reached! You can buy the laptop.")


#List .append(), insert(), remove(), pop(), clear(), sort()
#List append mean add something to the end of the list

print("----------Ex_1----------")
guests = []

name1 = input("Enter name 1: ")
guests.append(name1)
name2 = input("Enter name 2: ")
guests.append(name2)
name3 = input("Enter name 3: ")
guests.append(name3)

print(guests)
print("----------Ex_2----------")
sales = []

for i in range(5):
    amount = float(input("Enter sale amount: "))
    sales.append(amount)

print(sales)
print('----------Ex_3----------')
backpack = []   
item1 = input("Add item 1 to backpack: ")
backpack.append(item1)
item2 = input("Add item 2 to backpack: ")
backpack.append(item2)
item3 = input("Add item 3 to backpack: ")
backpack.append(item3)
print("Backpack contains:", backpack)

#List remove
print("----------Ex_1----------")
cart = ["apples", "milk", "bread", "eggs"]
input_item = input("Enter an item to remove from cart: ")
if input_item in cart:
    cart.remove(input_item)
    print(f"{input_item} removed from cart.")
print("Current cart:", cart)

print("----------Ex_2----------")
tasks = ["clean room", "wash dishes", "study python"]
completed_task = input("Enter a task you completed: ")
if completed_task in tasks:
    tasks.remove(completed_task)
    print(f"{completed_task} marked as completed.")
print("Remaining tasks:", tasks)

print("----------Ex_3----------")
subscribers = ["a@gmail.com", "b@gmail.com", "c@gmail.com"]
unsubscribe = input("Enter your email to unsubscribe: ")
if unsubscribe in subscribers:
    subscribers.remove(unsubscribe)
    print(f"{unsubscribe} has been unsubscribed.")
print("Current subscribers:", subscribers)

#POP
print("----------Ex_1----------")
history = ["clicked link", "typed text", "deleted image"]
last_action = history.pop()
print(f"Last action '{last_action}' undone.")
print("Current history:", history)

print("----------Ex_2----------")
queue = ["Person A", "Person B", "Person C"]
served = queue.pop(0)
print(f"{served} has been served.")
print("Current queue:", queue)

print("----------Ex_3----------")
cards = ["Ace", "King", "Queen", "Jack"]
top_card = cards.pop()
print(f"You drew the {top_card}.")
print("Remaining cards:", cards)

#clear 
print("----------Ex_1----------")
calculations = [10, 20, 30, 40]
calculations.clear()
print("Calculations cleared:", calculations)

print("----------Ex_2----------")
history = ["google.com", "youtube.com", "reddit.com"]
history.clear()
print("Browsing history cleared:", history)

print("----------Ex_3----------")
items = ["Glass", "shoes", "shirt"]
items.clear()
print("All items removed:", items)