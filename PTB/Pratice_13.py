print("--------------------------1. The Ice Cream Stand-----------------------")
# 1. The Ice Cream Stand (Input, Print, Operations)
# Form: Multiply input by a fixed variable 
# Scenario: You are working at a summer ice cream stand. 
# Task:
# Create a variable scoop_price (e.g., 2.50).
# Use input() to ask the customer "How many scoops would you like?".
# Convert that input into an integer.
# Calculate the total (scoop_price * quantity).
# Use print() to show a message like: "Your total is $7.50".
#answer
scoop_price = 2.50
quantity = int(input("How many scoops would you like? "))
total_cost = scoop_price * quantity
print(f"Your total is ${total_cost}.")

print("-----------------------2. The Bookstore Checkout-----------------------")
# 2. The Bookstore Checkout (Input, Print, Operations)
# Form: Multiply input by a fixed variable Scenario: You are selling comic books at a convention. 
# Task:
# Create a variable book_price (e.g., 15.00).
# Use input() to ask "How many comic books are you buying?".
# Convert that input into an integer.
# Calculate the total (book_price * quantity).
# Use print() to show a message like: "Your total is $45.0".
#answer 
book_price = 15.00
quantity = int(input("How many comic books are you buying? "))
total_cost = book_price * quantity
print(f"Your total is ${total_cost}.")

print("-----------------------3. The Arcade Game Score-----------------------")
# 3. The Top 3 High Scores (Lists, .append, Loop)
# Form: Empty list, loop 3 times, input inside, append Scenario: An arcade game needs to record the top 3 players of the day.
#  Task:
# Create an empty list called high_scores = [].
# Create a for loop that runs 3 times (using range(3)).
# Inside the loop, ask the user for a "Player Initials".
# Use .append() to add those initials to your high_scores list.
# At the end (outside the loop), print the full list of high scores.
#answer
high_scores = []
for i in range(3):
    initials = input("Enter Player Initials: ")
    high_scores.append(initials)
print("Today's top players are:", high_scores)

print("------------------------4. The Movie Theater Ticket Counter-----------------------")
# 4. The Daily Menu Board (Lists, .append, Loop)
# Form: Empty list, loop 3 times, input inside, append Scenario: A chef needs to write 3 special dishes on the daily menu board. 
# Task:
# Create an empty list called daily_specials = [].
# Create a for loop that runs 3 times (using range(3)).
# Inside the loop, ask the user for a "Dish Name".
# Use .append() to add that dish to your daily_specials list.
# At the end (outside the loop), print the full list of daily specials.
#answer 
daily_specials = []
for i in range(3):
    dish = input("Enter Dish Name: ")
    daily_specials.append(dish)
print("Today's specials are:", daily_specials)

print("------------------------5. The Secret Code Lock-----------------------")
# 5. The WiFi Login (While Loop, Input)
# Form: Secret variable, empty guess, while guess != secret, input inside Scenario: A user is trying to connect to a cafe's secure WiFi network. 
# Task:
# Define a variable wifi_password = "cafe2024".
# Create a variable user_entry and set it to an empty string "".
# Create a while loop that runs as long as user_entry is not equal (!=) to wifi_password.
# Inside the loop, use input() to update user_entry.
# After the loop finishes, print "Connected to WiFi!".
#answer
wifi_password = "cafe2024"
user_entry = ""
while user_entry != wifi_password:
    user_entry = input("Enter WiFi password: ")
print("Connected to WiFi!")

print("-------------------------6. The Secret Base Door-----------------------")
# 6. The Secret Base Door (While Loop, Input)
# Form: Secret variable, empty guess, while guess != secret, input inside Scenario: A spy needs to speak the correct voice code to enter a hidden base. Task:
# Define a variable voice_code = "eagle".
# Create a variable spoken_word and set it to an empty string "".
# Create a while loop that runs as long as spoken_word is not equal (!=) to voice_code.
# Inside the loop, use input() to update spoken_word.
# After the loop finishes, print "Welcome to the base!".
#answer
voice_code = "eagle"
spoken_word = ""
while spoken_word != voice_code:
    spoken_word = input("Speak the voice code: ")
print("Welcome to the base!")

print("-------------------------7. The Spam Inbox-----------------------")
# 7. The Spam Inbox (Lists, .clear)
# Form: List with 3 items, print, clear, print empty Scenario: Your email is full of junk mail, and you click the "Empty Spam" button. 
# Task:
# Create a list with some items: spam_folder = ["Lottery Win", "Cheap Meds", "Free Gift"].
# Print "Deleting all spam...".
# Use the .clear() method to empty the list.
# Print the folder again to confirm it is empty (it should show []).
#answer
spam_folder = ["Lottery Win", "Cheap Meds", "Free Gift"]
print("Deleting all spam...")
spam_folder.clear()
print(spam_folder)

print("-------------------------8. The Classroom Whiteboard-----------------------")
# 8. The Classroom Whiteboard (Lists, .clear)
# Form: List with 3 items, print, clear, print empty Scenario: Class is over, and the teacher needs to wipe the whiteboard clean for the next lesson. 
# Task:
# Create a list with some items: whiteboard = ["Math equation", "Drawing", "Homework notes"].
# Print "Class dismissed!".
# Use the .clear() method to empty the list.
# Print the whiteboard again to confirm it is empty (it should show []).
#answer
whiteboard = ["Math equation", "Drawing", "Homework notes"]
print("Class dismissed!")
whiteboard.clear()
print(whiteboard)


print("-------------------------9. The Egg Carton Packer-----------------------")
# 9. The Egg Carton Packer (def Function, Operations)
# Form: Function takes 1 param, multiply by 12 Scenario: A farm needs to calculate the total number of single eggs based on how many dozens they packed. 
# Task:
# Define a function named calculate_total_eggs that takes one parameter: dozens.
# Inside the function, multiply dozens by 12 and store it in a variable called total_eggs.
# Print a message inside the function: "Total single eggs: [amount]".
# Call the function at the bottom of your code with a number, for example: calculate_total_eggs(5).
#answer
def calculate_total_eggs(dozens):
    total_eggs = dozens * 12
    print(f"Total single eggs: {total_eggs}")
calculate_total_eggs(5)

print("-------------------------10. The Yearly Rent Calculator-----------------------")
# 10. The Yearly Rent Calculator (def Function, Operations)
# Form: Function takes 1 param, multiply by 12 Scenario: A real estate agent needs to show clients how much rent they will pay for a full 12-month lease. Task:
# Define a function named calc_yearly_rent that takes one parameter: monthly_rent.
# Inside the function, multiply monthly_rent by 12 and store it in a variable called yearly_total.
# Print a message inside the function: "Total rent for the year is: [amount]".
# Call the function at the bottom of your code with a number, for example: calc_yearly_rent(1500).
#answer
def calc_yearly_rent(monthly_rent):
    yearly_total = monthly_rent * 12
    print(f"Total rent for the year is: ${yearly_total}")
calc_yearly_rent(1500)

print("-------------------------11. The Hydration Tracker-----------------------")
# 11. The Hydration Tracker (While Loop, Operations)
# Form: Accumulator variable, while loop < target, input float, add to accumulator Scenario: A health app requires you to drink 2000 milliliters of water a day. 
# Task:
# Create a variable water_drunk = 0.
# Create a while loop that runs as long as water_drunk < 2000.
# Inside the loop, ask input(): "How many ml of water did you drink? ".
# Convert the input to a float and add it to water_drunk (use water_drunk = water_drunk + amount).
# Print the new current total inside the loop.
# After the loop finishes, print "Hydration goal reached!".
#answer
water_drunk = 0
while water_drunk < 2000:
    amount = float(input("How many ml of water did you drink? "))
    water_drunk += amount
    print(f"Current total: {water_drunk} ml")
print("Hydration goal reached!")

print("-------------------------12. The Vacation Fund-----------------------")
# 12. The Vacation Fund (While Loop, Operations)
# Form: Accumulator variable, while loop < target, input float, add to accumulator Scenario: You need $500 for a weekend beach trip and will keep saving until you hit the mark. Task:
# Create a variable vacation_fund = 0.
# Create a while loop that runs as long as vacation_fund < 500.
# Inside the loop, ask input(): "Deposit amount: ".
# Convert the input to a float and add it to vacation_fund (use vacation_fund = vacation_fund + amount).
# Print the new current balance inside the loop.
# After the loop finishes, print "Goal reached! Time to pack your bags."
vacation_fund = 0
while vacation_fund < 500:
    amount = float(input("Deposit amount: "))
    vacation_fund += amount
    print(f"Current balance: ${vacation_fund}")
print("Goal reached! Time to pack your bags.")

print("-------------------------13. The Post Office Sorter-----------------------") \
# 13. The Post Office Sorter (Lists, .append, For Loop)
# Form: Empty list, full list of 3 items, loop through full list, append to empty list Scenario: You are taking mail from a big drop bag and organizing it into the delivery system. 
# Task:
# Start with an empty list: delivery_system = [].
# Create a list of items: mail_bag = ["Letter", "Package", "Postcard"].
# Create a for loop that goes through mail_bag.
# Inside the loop, use .append() to move the item into your delivery_system list.
# Inside the loop, print "Sorted [item] for delivery".
# Finally, print the full delivery_system list.
delivery_system = []
mail_bag = ["Letter", "Package", "Postcard"]

for item in mail_bag:
    delivery_system.append(item)
    print(f"Sorted {item} for delivery")
print("Delivery system:", delivery_system)

print("-------------------------14. The Washing Machine-----------------------")
# 14. The Washing Machine (Lists, .append, For Loop)
# Form: Empty list, full list of 3 items, loop through full list, append to empty list Scenario: You are taking dirty clothes from a basket and putting them into the washing machine. 
# Task:
# Start with an empty list: washing_machine = [].
# Create a list of items: laundry_basket = ["Shirt", "Pants", "Socks"].
# Create a for loop that goes through laundry_basket.
# Inside the loop, use .append() to move the item into your washing_machine list.
# Inside the loop, print "Put [item] in the wash".
# Finally, print the full washing_machine list.
washing_machine = []
laundry_basket = ["Shirt", "Pants", "Socks"]

for item in laundry_basket:
    washing_machine.append(item)
    print(f"Put {item} in the wash")
print("Washing machine contents:", washing_machine)

print("-------------------------15. The Notification Clearer-----------------------")
# 15. The Notification Clearer (List, .clear)
# Form: List with 3 items, print current, input to delete, clear, print empty Scenario: Your phone has several annoying alerts. You click a button to dismiss them all at once. 
# Task:
# Create a list: notifications = ["Missed call", "New message", "System update"].
# Print "Current alerts:", followed by the list.
# Simulate the user clicking dismiss by asking an input(): "Type 'DISMISS' to clear all: ".
# (Optional challenge: Use an if statement to check if they typed "DISMISS").
# Run notifications.clear().
# Print "Alerts remaining:", followed by the notifications variable (it should be empty).
notifications = ["Missed call", "New message", "System update"]
print("Current alerts:", notifications)
user_input = input("Type 'DISMISS' to clear all: ")
if user_input == "DISMISS":
    notifications.clear()
    print("All alerts dismissed.")
print("Alerts remaining:", notifications)

print("-------------------------16. The Temp File Cleaner-----------------------")
# 16. The Temp File Cleaner (List, .clear)
# Form: List with 3 items, print current, input to delete, clear, print empty Scenario: Your computer is running out of space, so you use a tool to delete temporary junk files. 
# Task:
# Create a list: temp_files = ["cache.tmp", "log.txt", "data.bak"].
# Print "Junk files found:", followed by the list.
# Simulate the user running the tool by asking an input(): "Type 'CLEAN' to free up space: ".
# (Optional challenge: Use an if statement to check if they typed "CLEAN").
# Run temp_files.clear().
# Print "Junk files remaining:", followed by the temp_files variable (it should be empty).
temp_files = ["cache.tmp", "log.txt", "data.bak"]
print("Junk files found:", temp_files)  
user_input = input("Type 'CLEAN' to free up space: ")
if user_input == "CLEAN":
    temp_files.clear()
    print("Temporary files cleaned.")
print("Junk files remaining:", temp_files)

print("-------------------------17. The Square Pizza Sizer-----------------------")
# 17. The Square Pizza Sizer (def Function, Operations)
# Form: Function takes 1 param, multiply param by itself, print, call 3 times Scenario: A unique pizzeria only sells perfectly square pizzas. You need a function to calculate their size in square inches. 
# Task:
# Define a function called pizza_area that accepts one parameter: side_length.
# Inside the function, do the math: area = side_length * side_length.
# Inside the function, use print() to show: "The pizza is [area] square inches".
# Call your function three times with different numbers (e.g., pizza_area(8), pizza_area(10), pizza_area(12)).
def pizza_area(side_length):
    area = side_length * side_length
    print(f"The pizza is {area} square inches")
pizza_area(8)
pizza_area(10)
pizza_area(12)

print("-------------------------18. The Tile Size Calculator-----------------------")
# 18. The Tile Size Calculator (def Function, Operations)
# Form: Function takes 1 param, multiply param by itself, print, call 3 times Scenario: A construction worker needs to quickly calculate the area of square ceramic tiles. 
# Task:
# Define a function called calc_tile_size that accepts one parameter: edge_length.
# Inside the function, do the math: size = edge_length * edge_length.
# Inside the function, use print() to show: "The tile covers [size] square cm".
# Call your function three times with different numbers (e.g., calc_tile_size(30), calc_tile_size(45), calc_tile_size(60)).

def calc_tile_size(edge_length):
    size = edge_length * edge_length
    print(f"The tile covers {size} square cm")
calc_tile_size(30)
calc_tile_size(45)
calc_tile_size(60)

print("-------------------------19. The Boarding Pass-----------------------")
# 19. The Boarding Pass (Input, Print, Formatting)
# Form: 3 inputs, f-string formatting Scenario: An airline kiosk is printing a boarding pass for a passenger. 
# Task:
# Use input() to ask for "Passenger Name".
# Use input() to ask for "Destination".
# Use input() to ask for "Seat Number".
# Create a formatted print statement using an f-string to say: "Boarding Pass: {Passenger Name} flying to {Destination}, Seat {Seat Number}."

passenger_name = input("Passenger Name: ")  
destination = input("Destination: ")
seat_number = input("Seat Number: ")
print(f"Boarding Pass: {passenger_name} flying to {destination}, Seat {seat_number}.")

print("-------------------------20. The Gym Membership-----------------------")
# 20. The Gym Membership (Input, Print, Formatting)
# Form: 3 inputs, f-string formatting Scenario: A fitness center is creating a customized welcome screen for new members. Task:
# Use input() to ask for "Member Name".
# Use input() to ask for "Workout Goal" (e.g., Weight loss, Muscle gain).
# Use input() to ask for "Preferred Trainer".
# Create a formatted print statement using an f-string to say: "Welcome {Member Name}! Your goal is {Workout Goal} with trainer {Preferred Trainer}."
member_name = input("Member Name: ")
workout_goal = input("Workout Goal: ")
preferred_trainer = input("Preferred Trainer: ")
print(f"Welcome {member_name}! Your goal is {workout_goal} with trainer {preferred_trainer}.")
