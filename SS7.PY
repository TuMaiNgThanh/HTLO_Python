# i = 1
# while i < 7:
#     print("Hello world")
#     i +=1

# name = input("Enter your name: ")
# math = float(input("Enter math score: "))
# while math < 0 or math > 10:
#     print("Invalid score. Please enter a score between 0 and 10.")
#     math = float(input("Enter math score: "))
# english = float(input("Enter english score: "))
# while english < 0 or english > 10:
#     print("Invalid score. Please enter a score between 0 and 10.")
#     english = float(input("Enter english score: "))
# infomatics = float(input("Enter informatics score: "))
# while infomatics < 0 or infomatics > 10:
#     print("Invalid score. Please enter a score between 0 and 10.")
#     infomatics = float(input("Enter informatics score: "))
# gpa = (math + english + infomatics) / 3
# print(f"Student name: {name}")
# print(f"GPA: {gpa:.2f}")


# gpa = float(input("Enter your GPA: "))
# while gpa < 0 or gpa > 4.0:
#     print(" Invalid GPA. Please enter a GPA between 0 and 4.0")
#     gpa = float(input("Enter your GPA: "))
# if gpa >= 3.5:
#     print("Excellent")
# elif gpa >= 3.0:
#     print("Good")
# elif gpa >= 2.0:
#     print("Average")
# else:
#     print("Poor")

n = int(input("Enter a positive number n: "))
while n < 0:
    print("Invalid input. Please enter a positive number.")
    n = int(input("Enter a positive number n: "))
for i in range(n,101):
    print(i)
print("Done!")