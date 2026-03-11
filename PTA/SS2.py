# def calculate(numbers):
#     total = sum(numbers)
#     average = total / len(numbers)
#     return average

# data = [5,10,15,20,25]
# result = int(calculate(data))
# print (result)

# cat = "Meow"
# dog = "Woof"
# dog = "Gau Gau"
# dog = "Woof"
# dog = "ACHOOO" \
# ""


# def Chop():
#     age = 0
#     name = ""
#     gender = ""
#     color = ""
#     weight = 0

# class Vatnuoi:
#     def __init__(self, name, age, gender, color, weight):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.color = color
#         self.weight = weight

# Vatnuoi1 = Vatnuoi("Chop", 5, "Male", "Brown", 10)  
# Vatnuoi2 = Vatnuoi("Miu", 3, "Female", "White", 5)

# print(Vatnuoi1.name, Vatnuoi1.age, Vatnuoi1.gender, Vatnuoi1.color, Vatnuoi1.weight)
# print(Vatnuoi2.name, Vatnuoi2.age, Vatnuoi2 .gender, Vatnuoi2.color, Vatnuoi2.weight)

# class car:
#     def __init__(self, brand, model, year, color, seats):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.color = color
#         self.seats = seats

# car1 = car("Toyota", "Camry", 2020, "Red", 5)
# car2 = car("RR", "Phantom", 2021, "Black", 4)

# print(car1.brand, car1.model, car1.year, car1.color, car1.seats)
# print(car2.brand, car2.model, car2.year, car2.color, car2.seats)

# print(f"Car: {car1.brand} {car1.model}")


# class human:
#     def __init__(self, name, age, gender, eyes, hair_color):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.eyes = eyes
#         self.hair_color = hair_color

# Alice = human("Alice", 30, "Female", "Blue", "Blonde")
# print(f"Name: {Alice.name}")
# print(f"Age: {Alice.age}")
# print(f"Gender: {Alice.gender}")
# print(f" Eyes: {Alice.eyes}")
# print(f"Hair Color: {Alice.hair_color}")

# class Cat:
#     def __init__(self, name, age, breed, color, weight):
#         self.name = name
#         self.age = age
#         self.breed = breed
#         self.color = color
#         self.weight = weight

# Milu = Cat("Milu", 3, "Siamese", "Cream", 5)
# print(f"Name: {Milu.name}")
# print(f"Age: {Milu.age}")
# print(f"Breed: {Milu.breed}")
# print(f"Color: {Milu.color}")
# print(f"Weight: {Milu.weight}")

# class Student:
#     def __init__(self, name, age, grade, class_name):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.class_name = class_name

# An = Student("An", 12, 6, "Grade 6")
# print(f"Name: {An.name}")
# print(f"Age: {An.age}")
# print(f"Grade: {An.grade}")
# print(f"Class Name: {An.class_name}")

# Viết chương trình xây dựng một lớp Quản lý điểm học sinh gồm các thuộc tính: 
# HoTen 
# Lop 
# Truong 
# DiemToan 
# DiemVan 
# DiemAnh 
#Hãy gán xây dựng dữ liệu cho ít nhất 3 học sinh thông qua lớp QuanLyDiemHS. 
# Xử lý và xuất ra màn hình thông tin của học sinh có điểm trung bình ba môn Toán,  Văn và Anh cao nhất. 
# Nếu có nhiều học sinh có điểm trung bình của ba môn bằng nhau, hãy xuất ra thông tin của tất cả các học sinh đó.
# class QuanLyDiemHS: 
class QLHS:
    full_name = ""
    age = 0
    grade = 0
    school = ""
    Math_score = 0
    Literature_score = 0
    English_score = 0

student1 = QLHS()
student1.full_name = "An"
student1.age = 12
student1.grade = 6
student1.school = "Grade 6"
student1.Math_score = 8
student1.Literature_score = 9
student1.English_score = 7

student2 = QLHS()
student2.full_name = "Binh"
student2.age = 13
student2.grade = 7
student2.school = "Grade 7"
student2.Math_score = 7
student2.Literature_score = 8
student2.English_score = 9

student3= QLHS()
student3.full_name = "Cuong"
student3.age = 14
student3.grade = 8
student3.school = "Grade 8"
student3.Math_score = 9
student3.Literature_score = 7
student3.English_score = 8

