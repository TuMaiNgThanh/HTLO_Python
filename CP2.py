# s = 0 
# for i in range(2, 101): 
#     is_prime = True 
#     for j in range(2, i): 
#         if i % j == 0: 
#             is_prime = False 
#     if is_prime: 
#         s += i
#         print(i, end = " ") 
# print(f"\nTổng của các số nguyên tố bé hơn 100 là: {s} ")


n = int(input("Enter a positive integer N: "))
sum = 0
for i in range (2,n+1,2):
    print(i, end = " + ")
    sum+=i
print(f"\nTotal: {sum}")