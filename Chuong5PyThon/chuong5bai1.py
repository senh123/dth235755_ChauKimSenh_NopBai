def CheckDoiXung(s):
    flag = True
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            flag = False
            break
    return flag

def main():
    s = input("Nhập 1 chuỗi: ")
    if CheckDoiXung(s):
        print("👉 Chuỗi bạn nhập là **đối xứng**!")
    else:
        print("❌ Chuỗi bạn nhập **không đối xứng**.")

# Vòng lặp chính
while True:
    main()
    s = input("Tiếp không Thím? (c/k): ")
    if s.lower() == "k":
        break

print("CÁM ƠN THÍM 💖")
