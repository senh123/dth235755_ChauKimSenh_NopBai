'''Cho i, j, k là các con số và lệnh dưới đây:
        if i<j:
                 if j<k:
                         i=j
                 else :
                         j=k
        else:                           
                if j>k:
                    j=i
                    else :
                        i=k
                print("i=",i,"j=",j,"k=",k)
Hãy cho biết kết quả xuất ra màn hình nếu tuần tự 3 biến trên có các giá trị sau:
(a) i = 3, j = 5, and k = 7
(b) i = 3, j = 7, and k = 5
(c) i = 5, j = 3, and k = 7
(d) i = 5, j = 7, and k =3
(e) i = 7, j = 3, and k = 5
(f) i =7, j = 5, and k = 3
'''
#BaiLam:
'''
(a) i = 3, j = 5, and k = 7:
i < j → 3 < 5 → True

vào if j < k: 5 < 7 → True

thực hiện: i = j → i = 5

kết quả: i=5, j=5, k=7
(b) i = 3, j = 7, and k = 5:
i < j → 3 < 7 → True

vào if j < k: 7 < 5 → False

thực hiện: j = k → j = 5

kết quả: i=3, j=5, k=5
(c) i = 5, j = 3, and k = 7:
i < j → 5 < 3 → False

vào else:

if j > k: 3 > 7 → False

thực hiện: i = k → i = 7

kết quả: i=7, j=3, k=7
(d) i = 5, j = 7, and k =3:
i < j → 5 < 7 → True

vào if j < k: 7 < 3 → False

thực hiện: j = k → j = 3

kết quả: i=5, j=3, k=3
(e) i = 7, j = 3, and k = 5:
i < j → 7 < 3 → False

vào else:

if j > k: 3 > 5 → False

thực hiện: i = k → i = 5

kết quả: i=5, j=3, k=5
(f) i =7, j = 5, and k = 3:
i < j → 7 < 5 → False

vào else:

if j > k: 5 > 3 → True

thực hiện: j = i → j = 7

kết quả: i=7, j=7, k=3
'''