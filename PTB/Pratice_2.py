print("-----------------------1. The Movie Theater Ticket Booth-----------------------")
# 1. The Movie Theater Ticket Booth (Input, Print, Operations)
# Scenario: You are writing the software for a local cinema. Task:
# Create a variable ticket_price (e.g., 12.50).
# Use input() to ask the user "How many tickets do you need?".
# Convert that input into an integer.
# Calculate the total_cost (ticket_price * quantity).
# Use print() to show a message like: "Your total cost is $25.0".
#answer
ticket_price = 12.50
quantity = int(input("How many tickets do you need? "))
total_cost = ticket_price * quantity
print(f"Your total cost is ${total_cost}.")

print("------------------------2. The Esports Team Roster-----------------------")
# 2. The Esports Team Roster (Lists, .append, Loop)
# Scenario: You are the manager of a new gaming team and need to register your players. Task:
# Create an empty list called team_roster = [].
# Create a for loop that runs 3 times (using range(3)).
# Inside the loop, ask the user for a "Player Nickname".
# Use .append() to add that nickname to your team_roster list.
# At the end (outside the loop), print the full team roster.

team_roster = []
for i in range(3):
    nickname = input("Enter Player Nickname: ")
    team_roster.append(nickname)
print("Your team roster is:", team_roster)

print("------------------------3. The Smartphone Lock Screen-----------------------")
# 3. The Smartphone Lock Screen (While Loop, Input)
# Scenario: A phone screen needs to keep asking for a PIN code until the user enters the correct one. Task:
# Define a variable correct_pin = "9999".
# Create a variable user_attempt and set it to an empty string "".
# Create a while loop that runs as long as user_attempt is not equal (!=) to correct_pin.
# Inside the loop, use input() to ask for the PIN and update user_attempt.
# After the loop finishes (meaning they got it right), print "Phone Unlocked!".
correct_pin = "9999"
user_attempt = ""
while user_attempt != correct_pin:
    user_attempt = input("Enter PIN: ")
print("Phone Unlocked!")

print("------------------------4. The Daily To-Do List Reset-----------------------")
# 4. The Daily To-Do List Reset (Lists, .clear)
# Scenario: It's midnight, and your productivity app needs to wipe yesterday's completed tasks to start fresh. Task:
# Create a list with some tasks: daily_tasks = ["Read a book", "Walk the dog", "Do homework"].
# Print "Day is over! Great job.".
# Use the .clear() method to empty the list.
# Print the task list again to confirm it is empty (it should show []).
daily_tasks = ["Read a book", "Walk the dog", "Do homework"]
print("Day is over! Great job.")
daily_tasks.clear()
print(daily_tasks)

print("-------------------------5. The Streaming Subscription Calculator-----------------------")

# 5. The Streaming Subscription Calculator (def Function, Operations)
# Scenario: Your app helps users figure out how much they spend on streaming services per year. Task:
# Define a function named calculate_annual_cost that takes one parameter: monthly_fee.
# Inside the function, multiply monthly_fee by 12 and store it in a variable called annual_cost.
# Print a message inside the function: "Your total yearly cost is: [amount]".
# Call the function at the bottom of your code with a number, for example: calculate_annual_cost(15).
def calculate_annual_cost(monthly_fee):
    annual_cost = monthly_fee * 12
    print(f"Your total yearly cost is: ${annual_cost}")
calculate_annual_cost(15)

print("-------------------------6. The Fitness Distance Tracker-----------------------")
# 6. The Fitness Distance Tracker (While Loop, Operations)
# Scenario: You are training for a 42-kilometer marathon. You need a program that tracks your training runs until you hit your distance goal. Task:
# Create a variable kilometers_run = 0.
# Create a while loop that runs as long as kilometers_run < 42.
# Inside the loop, ask input(): "How many kilometers did you run today? ".
# Convert the input to a float and add it to kilometers_run (using kilometers_run = kilometers_run + distance).
# Print the total distance covered so far inside the loop.
# After the loop finishes, print "Congratulations! You reached your marathon goal distance!"
kilometers_run = 0
while kilometers_run < 42:  
    distance = float(input("How many kilometers did you run today? "))
    kilometers_run += distance
    print(f"Total distance covered so far: {kilometers_run} km")
print("Congratulations! You reached your marathon goal distance!")


print("-------------------------7. The Digital Playlist Maker-----------------------")
# 7. The Digital Playlist Maker (Lists, .append, For Loop)
# Scenario: You are downloading a new album and want to move the songs into your personal "Favorites" playlist. Task:
# Start with an empty list: favorites_playlist = [].
# Create a list of downloaded songs manually: new_album = ["Song A", "Song B", "Song C"].
# Create a for loop that goes through new_album.
# Inside the loop, use .append() to move the song into your favorites_playlist.
# Inside the loop, print "Added [song] to favorites".
# Finally, print the full favorites playlist.

favorites_playlist = []
new_album = ["Song A", "Song B", "Song C"]
for song in new_album:
    favorites_playlist.append(song)
    print(f"Added {song} to favorites")
print("Your favorites playlist is:", favorites_playlist)

print("-------------------------8. The Chat History Wiper-----------------------")
# 8. The Chat History Wiper (List, .clear)
# Scenario: You are building a secure messaging app. If the user types "WIPE", all messages in the current chat are permanently deleted. Task:
# Create a list: chat_log = ["Hi!", "How are you?", "Secret meeting at 5 PM"].
# Print "Current chat:", followed by the list.
# Simulate the user wanting privacy by asking an input(): "Type 'WIPE' to delete conversation: ".
# (Optional challenge: Use an if statement to check if they typed "WIPE").
# Run chat_log.clear().
# Print "Chat log is now:", followed by the chat_log variable (it should be empty).

chat_log = ["Hi!", "How are you?", "Secret meeting at 5 PM"]
print("Current chat:", chat_log)
user_input = input("Type 'WIPE' to delete conversation: ")
if user_input == "WIPE":
    chat_log.clear()
    print("Chat history wiped.")
print("Chat log is now:", chat_log)

print("-------------------------9. The Travel Budget Converter-----------------------")
# 9. The Travel Budget Converter (def Function, Operations)
# Scenario: You are building a travel app that converts US Dollars to another currency (e.g., Euros, where 1 USD is roughly 0.93 EUR). Task:
# Define a function called convert_to_euros that accepts one parameter: usd_amount.
# Inside the function, do the math: euros = usd_amount * 0.93.
# Inside the function, use print() to show: "That equals [euros] Euros".
# Call your function three times with different amounts (e.g., convert_to_euros(10), convert_to_euros(50), convert_to_euros(100)).

def convert_to_euros(usd_amount):
    euros = usd_amount * 0.93
    print(f"That equals {euros} Euros")
convert_to_euros(10)
convert_to_euros(50)
convert_to_euros(100)

print("------------------------10. The Video Game Character Creator-----------------------")
# 10. The Video Game Character Creator (Input, Print, Formatting)
# Scenario: A player is starting a new RPG game. You need to gather their stats and print a welcome banner. Task:
# Use input() to ask for "Character Name".
# Use input() to ask for "Character Class" (e.g., Warrior, Mage).
# Use input() to ask for "Starting Level".
# Create a formatted print statement using an f-string to say: "Welcome, {Character Name} the {Character Class}! You are starting at level {Starting Level}."
# (Note: If you haven't learned f-strings yet, you can use commas: print("Welcome", character_name...))

character_name = input("Character Name: ")
character_class = input("Character Class (e.g., Warrior, Mage): ")
starting_level = input("Starting Level: ")
print(f"Welcome, {character_name} the {character_class}! You are starting at level {starting_level}.")



print("------------------------11. The String Builder-----------------------")
# Viết một hàm có tham số truyền vào là một xâu ký tự. Hãy xử lý và hiển thị các bước tạo thành xâu ban đầu. Mỗi bước sẽ hiển thị một phần của xâu theo cấu trúc tăng dần 
# translate: Write a function that takes a string as a parameter. Process and display the steps of building the original string. Each step will show a part of the string in an increasing structure.

def display_string_steps(input_string):
    for i in range(1, len(input_string) + 1):
        print(input_string[:i])
display_string_steps("MindX")


print("-------------------------12. The Weighted Average Calculator-----------------------")
# Viết một hàm có tham số truyền vào là một danh sách điểm số môn Tin học của An. Hãy xử lý và in ra màn hình điểm trung bình môn Tin học của An, trong đó điểm cuối cùng trong danh sách điểm có hệ số là 2. 
# translate: Write a function that takes a list of An's computer science scores as a parameter. Process and print An's average computer science score, where the last score in the list has a weight of 2.
def calculate_average_with_weighted_last(scores):
    if not scores:
        return 0
    total = sum(scores[:-1])  # Tổng các điểm trừ điểm cuối cùng
    weighted_last = scores[-1] * 2  # Điểm cuối cùng nhân với hệ số 2
    total += weighted_last
    average = total / (len(scores) + 1)  # Tổng số điểm chia cho tổng số hệ số (các điểm trước đó có hệ số 1, điểm cuối có hệ số 2)
    print(f"Điểm trung bình môn Tin học của An là: {average}")
calculate_average_with_weighted_last([8, 9, 7, 10])