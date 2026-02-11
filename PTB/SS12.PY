# def hello():
#     print("Hello, World!")
#     print("Chao mung den voi SS12.py")

# hello()

# def greeting():
#     name = input("Nhap ten cua ban: ")
#     print("Xin chao, " + name + "!")
# greeting()

# def absolute_value():
#     num = int(input("Nhap mot so nguyen: "))
#     if num < 0:
#         absolute = -num
#     else:
#         absolute = num
#     print("Gia tri tuyet doi la:", absolute)

# absolute_value()


# def infomation(name, age, birthday):
#     print("Name:", name)
#     print("Age:", age)
#     print("Birth:", birthday)

# name = input("Write your name: ")
# age = int(input("Write your age: "))
# birthday = int(input("Write your birthday: "))

# infomation(name, age, birthday)

# def list_and_sum(danh_sach):
#     print('Danh sach trong cac phan tu')
#     for so in danh_sach:
#         print(so)   
#     tong = sum(danh_sach)
#     print("Tong cac phan tu trong danh sach la:", tong)

# danh_sach = []
# n = int(input("Nhap so luong phan tu trong danh sach: "))
# for i in range(n):
#     so = int(input("Nhap phan tu thu {}: ".format(i+1)))
#     danh_sach.append(so)
# list_and_sum(danh_sach)

# def total_sum(a, b):
#     sum = 0
#     for i in range(a, b + 1):
#         sum += i
#     print("sum for", a, "to", b, ": ", sum)

# n = int( input ( "Write a positive integer: ") )
# total_sum(1, n)
# total_sum(1, n//2)
# total_sum(n//2, n)

#Viet chuơng trình nhap vao 4 so nguyen lan luợt la tử
#và mãu của hai phân sỗ, khởi tạo hàm tính tổng và rút
#gọn phân số và xuất ra màn hình.

# from math import gcd
# def rut_gon_phan_so(tu, mau):
#     ucln = gcd(tu, mau)
#     tu_rut_gon = tu // ucln
#     mau_rut_gon = mau // ucln
#     return tu_rut_gon, mau_rut_gon
# tu = int(input("Nhap tu so: "))
# mau = int(input("Nhap mau so: "))
# tu_rut_gon, mau_rut_gon = rut_gon_phan_so(tu, mau)
# print("Phan so rut gon la: {}/{}".format(tu_rut_gon, mau_rut_gon))

# rut_gon_phan_so(8, 12)

#EX1
def multiplication_table(number):
    print(f"--- Table of {number} ---")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

multiplication_table(5)

#EX2
def check_voting_eligibility(age):
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

check_voting_eligibility(18)


#EX3
def km_to_meters(km):
    meters = km * 1000  
    print(f"{km} km is equal to {meters} meters.")
km_to_meters(5)

#EX4
def add_numbers(a,b):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    sum = a + b
    print(f"{a} + {b} = {sum}.")

add_numbers(3,4)


#EX5  
def check_number(number):
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

check_number(4)
