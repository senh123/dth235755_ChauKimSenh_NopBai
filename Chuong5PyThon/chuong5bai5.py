import re

def NegativeNumberInStrings(s):
    # Tìm tất cả các số âm trong chuỗi (dạng -5, -12, -100, ...)
    numbers = re.findall(r'-\d+', s)
    # Chuyển chuỗi số sang kiểu int
    negatives = [int(x) for x in numbers]
    # Xuất kết quả
    if negatives:
        print("Các số nguyên âm trong chuỗi là:", *negatives)
    else:
        print("Không có số nguyên âm nào trong chuỗi.")

# Chương trình chính
chuoi = input("Nhập chuỗi: ")
NegativeNumberInStrings(chuoi)
