import math

try:
    r = float(input("Nhập bán kính hình tròn: "))
    cv = 2 * math.pi * r
    dt = math.pi * r ** 2
    print("Chu vi là:", cv)
    print("Diện tích là:", dt)
except:
    print("Lỗi rồi")
