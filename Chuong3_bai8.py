# Nhập 2 số a, b
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

# Nhập phép toán
phep = input("Nhập phép toán (+, -, *, /): ")

# Xử lý phép toán
if phep == '+':
    ket_qua = a + b
elif phep == '-':
    ket_qua = a - b
elif phep == '*':
    ket_qua = a * b
elif phep == '/':
    if b == 0:
        print("Lỗi: Không thể chia cho 0!")
        ket_qua = None
    else:
        ket_qua = a / b
else:
    print("Phép toán không hợp lệ!")
    ket_qua = None

# In kết quả nếu hợp lệ
if ket_qua is not None:
    print(f"Kết quả: {a} {phep} {b} = {ket_qua}")
