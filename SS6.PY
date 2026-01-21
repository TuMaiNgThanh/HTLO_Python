# for j in range (1,10):
#     print(f"Bảng cửu chương {j} ")
#     for i in range (2,10,2):
#         print(f"{i} x {j} = {i*j}")
#     print("--------------")


# n = int(input("Nhập số nguyên dương n: "))
# total = 0
# for i in range(1, n+1):
#     total += i
# print("Tổng các số từ 1 đến", n, "là:", total)

# for i in range(1,8):
#     print(i)
#     for j in range(1,8):
#         print(j)


n = int(input("Nhập n: "))
m= int(input("Nhập m: "))
for i in range(0,n,1):
    for j in range(0,m,1):
        print("* ", end="")
    print()

