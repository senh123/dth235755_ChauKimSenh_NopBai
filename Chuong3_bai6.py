def doc_so(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi",
            "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    
    if n < 10:
        if n == 5:
            return "năm"
        else:
            return don_vi[n]
    else:
        hang_chuc = n // 10
        hang_dv = n % 10
        
        ket_qua = chuc[hang_chuc]
        
        if hang_dv == 0:
            return ket_qua
        elif hang_dv == 1:
            ket_qua += " mốt" if hang_chuc > 1 else " một"
        elif hang_dv == 5:
            ket_qua += " lăm"
        else:
            ket_qua += " " + don_vi[hang_dv]
        return ket_qua

try:
    n = int(input("Nhập số n (0-99): "))
    if 0 <= n <= 99:
        if n == 0:
            print("Không")
        else:
            print(doc_so(n).capitalize())
    else:
        print("Vui lòng nhập số từ 0 đến 99.")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
