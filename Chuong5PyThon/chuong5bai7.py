def ToiUuChuoi(s):
    s = s.strip()
    words = s.split()
    words = [word.capitalize() for word in words]
    s = " ".join(words)
    return s

chuoi = input("Nhập chuỗi danh từ: ")
print("Chuỗi sau khi tối ưu là:", ToiUuChuoi(chuoi))
