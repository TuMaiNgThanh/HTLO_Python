# a,b,c = input(int("Viet 3 chu so nguyen: "))
# while a>b or a>c or b>c:
#     print("Day ko phai la hinh tam giac")
#     a,b,c = input(int("Viet 3 chu so nguyen: "))
# print("Day la hinh tam giac")

thang = int(input("Nhập số tháng: "))
if(thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12):
    print("Thang nay có 31 ngay")
elif(thang == 4 or thang == 6 or thang == 9 or thang == 11):
    print("Thang này có 30 ngay")
elif(thang == 2):
    print("Tháng này có 28 hoac 29 ngày")
else:
    print("Khong đung so thang trong nam")