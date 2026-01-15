print((16-13//4)%4)
print(2**2**3)

a = 5
b = 10
c = (a < b) and (a+5 != b)
d = not (a*a + b*b <= 100)
e = (3*a > b) or (2*a == b)
print(c, d, e)

n = int(input("Nhập số kẹo trong túi: "))
m = int(input("Nhập số học sinh trong lớp: "))

so_keo_moi_hoc_sinh = n // m
keo_con_thua = n % m

print( "Số kẹo mỗi học sinh nhận được là:", so_keo_moi_hoc_sinh)
print( "Số kẹo còn thừa sau khi chia là:", keo_con_thua)

S = int (input ("Số giây: ") )

gio = S // 3600
so_giay_con_lai_sau_gio = S % 3600
phut = so_giay_con_lai_sau_gio // 60
giay = so_giay_con_lai_sau_gio % 60

print(gio, "giờ", phut, "phút", giay, "giây")