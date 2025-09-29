def ngay_ke_sau(ngay, thang, nam):
    # Số ngày tối đa từng tháng (chưa xét năm nhuận)
    ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Kiểm tra năm nhuận
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        ngay_trong_thang[1] = 29  # tháng 2 có 29 ngày
    
    ngay += 1  # Tăng ngày lên 1
    
    # Nếu vượt quá số ngày của tháng, sang tháng mới
    if ngay > ngay_trong_thang[thang - 1]:
        ngay = 1
        thang += 1
        # Nếu tháng vượt quá 12, sang năm mới
        if thang > 12:
            thang = 1
            nam += 1
    
    return ngay, thang, nam

# Nhập dữ liệu
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Kiểm tra dữ liệu nhập hợp lệ
if thang < 1 or thang > 12:
    print("Tháng không hợp lệ.")
else:
    # Kiểm tra năm nhuận để xác định số ngày trong tháng 2
    ngay_trong_thang = [31, 29 if (nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0)) else 28, 
                        31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if ngay < 1 or ngay > ngay_trong_thang[thang - 1]:
        print("Ngày không hợp lệ cho tháng đã nhập.")
    else:
        n, m, y = ngay_ke_sau(ngay, thang, nam)
        print(f"Ngày kế sau là: {n}/{m}/{y}")
