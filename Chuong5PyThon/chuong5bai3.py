def CheckPrime(x):
    if x < 2:
        return False
    for i in range(2, int(abs(x)**0.5) + 1):
        if x % i == 0:
            return False
    return True

s = input("Nhập chuỗi các số (phân tách bằng dấu ';'): ")
if s.strip() == "":
    s = "5;7;8;-2;8;11;-13;9;10"

arr = s.split(';')

sochan = 0
soam = 0
sont = 0
tong = 0

for x in arr:
    print(x)
    n = int(x)
    if n % 2 == 0:
        sochan += 1
    if n < 0:
        soam += 1
    if CheckPrime(n):
        sont += 1
    tong += n

print("Số chẵn =", sochan)
print("Số âm =", soam)
print("Số nguyên tố =", sont)
print("Trung bình =", tong / len(arr))
