"""
EXERCISE 1: Cho x,y,z=3,5,7. Hãy cho biết kết quả của Boolean Expression
a. x == 3               e. x != y - 2                   i. x >= 0 and x < 2
--> T                   --> F                           --> F
b. x < y                f. x < 10                       j. x < 0 or x < 10
--> T                   --> T                           --> T
c. x >= y               g. x >= 0 and x < 10            k. x > 0 or x < 10
--> F                   --> T                           --> T
d. x <= y               h. x < 0 and x < 10             l. x < 0 or x > 10
--> T                   --> F                           --> F
"""
print("*"*15,"EX1","*"*15)
x= 3
y=5
z=7
print(x==3,x<y,x >= y,x <= y,x != y - 2,x < 10,x >= 0 and x < 10, x < 0 and x < 10,
      x >= 0 and x < 2, x < 0 or x < 10, x > 0 or x < 10, x <0 or x > 10)

"""
EXERCISE 2: Cho i, j , k là các con số và lệnh dưới đây:
                if i < j:
                    if j < k:
                        i = j
                    else:
                        j = k
                else:
                    if j > k:
                        j = i
                    else:
                        i = k
                print("i = ", i," j = ",j," k = ",k)
            Hã̃y cho biết kq xuất ra màn hình nếu tuần tự 3 biến trên có giá trị sau:
                a. i=3, j=5, k=7                d. i=5, j=7, k=3
                --> i=5, j=5, k=7               --> i=5, j=3, k=3
                b. i=3, j=7, k= 5               e. i=7, j=3, k=5
                --> i=3, j=5, k=5               --> i=5, j=3, k=5
                c. i=5, j=3, k=7                f. i=7, j=5, k=3
                --> i=7, j=3, k=7               --> i=7, j=7, k=3
"""
print("*"*15,"EX2","*"*15)
i=float(input("Nhập i = "))
j=float(input("Nhập j = "))
k=float(input("Nhập k = "))
if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print("i = ", i," j = ",j," k = ",k)

"""
EXERCISE 3: Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ
            ví dụ: n = 35 --> Ba mươi lăm, n=5 --> năm
"""
print("*"*15,"EX3","*"*15)
print("Chương trình đọc số thành chữ!")
n=int(input("Nhập một số có tối đa 2 chữ số: "))
a=n//10
b=n%10
if (a >= 0 and a < 10) and (b >= 0 and b < 10):
    if a == 0:
        print("Không " if b == 0 else
              "Một" if b == 1 else
              "Hai" if b == 2 else
              "Ba" if b == 3 else
              "Bốn" if b == 4 else
              "Lăm" if b == 5 else
              "Sáu" if b == 6 else
              "Bảy" if b == 7 else
              "Tám" if b == 8 else
              "Chín")
    elif a == 1:
        print("Mười " if b == 0 else
              "Mười Một" if b == 1 else
              "Mười Hai" if b == 2 else
              "Mười Ba" if b == 3 else
              "Mười Bốn" if b == 4 else
              "Mười Lăm" if b == 5 else
              "Mười Sáu" if b == 6 else
              "Mười Bảy" if b == 7 else
              "Mười Tám" if b == 8 else
              "Mười Chín")
    elif a == 2:
        print("Hai Mươi " if b == 0 else
              "Hai Mươi Mốt" if b == 1 else
              "Hai Mươi Hai" if b == 2 else
              "Hai Mươi Ba" if b == 3 else
              "Hai Mươi Bốn" if b == 4 else
              "Hai Mươi Lăm" if b == 5 else
              "Hai Mươi Sáu" if b == 6 else
              "Hai Mươi Bảy" if b == 7 else
              "Hai Mươi Tám" if b == 8 else
              "Hai Mươi Chín")
    elif a == 3:
        print("Ba Mươi " if b == 0 else
              "Ba Mươi Mốt" if b == 1 else
              "Ba Mươi Hai" if b == 2 else
              "Ba Mươi Ba" if b == 3 else
              "Ba Mươi Bốn" if b == 4 else
              "Ba Mươi Lăm" if b == 5 else
              "Ba Mươi Sáu" if b == 6 else
              "Ba Mươi Bảy" if b == 7 else
              "Ba Mươi Tám" if b == 8 else
              "Ba Mươi Chín")
    elif a == 4:
        print("Bốn Mươi " if b == 0 else
              "Bốn Mươi Mốt" if b == 1 else
              "Bốn Mươi Hai" if b == 2 else
              "Bốn Mươi Ba" if b == 3 else
              "Bốn Mươi Bốn" if b == 4 else
              "Bốn Mươi Lăm" if b == 5 else
              "Bốn Mươi Sáu" if b == 6 else
              "Bốn Mươi Bảy" if b == 7 else
              "Bốn Mươi Tám" if b == 8 else
              "Bốn Mươi Chín")
    elif a == 5:
        print("Năm Mươi " if b == 0 else
              "Năm Mươi Mốt" if b == 1 else
              "Năm Mươi Hai" if b == 2 else
              "Năm Mươi Ba" if b == 3 else
              "Năm Mươi Bốn" if b == 4 else
              "Năm Mươi Lăm" if b == 5 else
              "Năm Mươi Sáu" if b == 6 else
              "Năm Mươi Bảy" if b == 7 else
              "Năm Mươi Tám" if b == 8 else
              "Năm Mươi Chín")
    elif a == 6:
        print("Sáu Mươi " if b == 0 else
              "Sáu Mươi Mốt" if b == 1 else
              "Sáu Mươi Hai" if b == 2 else
              "Sáu Mươi Ba" if b == 3 else
              "Sáu Mươi Bốn" if b == 4 else
              "Sáu Mươi Lăm" if b == 5 else
              "Sáu Mươi Sáu" if b == 6 else
              "Sáu Mươi Bảy" if b == 7 else
              "Sáu Mươi Tám" if b == 8 else
              "Sáu Mươi Chín")
    elif a == 7:
        print("Bảy Mươi " if b == 0 else
              "Bảy Mươi Mốt" if b == 1 else
              "Bảy Mươi Hai" if b == 2 else
              "Bảy Mươi Ba" if b == 3 else
              "Bảy Mươi Bốn" if b == 4 else
              "Bảy Mươi Lăm" if b == 5 else
              "Bảy Mươi Sáu" if b == 6 else
              "Bảy Mươi Bảy" if b == 7 else
              "Bảy Mươi Tám" if b == 8 else
              "Bảy Mươi Chín")
    elif a == 8:
        print("Tám Mươi " if b == 0 else
              "Tám Mươi Mốt" if b == 1 else
              "Tám Mươi Hai" if b == 2 else
              "Tám Mươi Ba" if b == 3 else
              "Tám Mươi Bốn" if b == 4 else
              "Tám Mươi Lăm" if b == 5 else
              "Tám Mươi Sáu" if b == 6 else
              "Tám Mươi Bảy" if b == 7 else
              "Tám Mươi Tám" if b == 8 else
              "Tám Mươi Chín")
    elif a == 9:
        print("Chín Mươi " if b == 0 else
              "Chín Mươi Mốt" if b == 1 else
              "Chín Mươi Hai" if b == 2 else
              "Chín Mươi Ba" if b == 3 else
              "Chín Mươi Bốn" if b == 4 else
              "Chín Mươi Lăm" if b == 5 else
              "Chín Mươi Sáu" if b == 6 else
              "Chín Mươi Bảy" if b == 7 else
              "Chín Mươi Tám" if b == 8 else
              "Chín Mươi Chín")
else:
    print("Số vừa nhập không hợp lệ!!!")

"""
EXERCISE 4: Nhập vào 1 ngày (ngày, tháng, năm). Tìm ngày kế sau ngày vừa nhập (ngày/tháng/năm)
"""
print("*"*15,"EX4","*"*15)
print("Chương trình tìm ngày kế tiếp")
d=int(input("Nhập ngày: "))
m=int(input("Nhập tháng: "))
y=int(input("Nhập năm: "))
if (d>0 and d<=31) and (m>0 and m<13) and y>0:
    print("Ngày vừa nhập: {0}/{1}/{2}".format(d,m,y))

    if m in (1,3,5,7,8,10,12):
        if d == 31:
            print("Ngày kế tiếp là: {0}/{1}/{2}".format(1,m+1,y))
        elif d < 31:
            print("Ngày kế tiếp là: {0}/{1}/{2}".format(d+1, m, y))
        else:
            print("Ngày không hợp lệ!")
    if m in (4,6,11):
        if d == 30:
            print("Ngày kế tiếp là: {0}/{1}/{2}".format(1, m + 1, y))
        elif d < 30:
            print("Ngày kế tiếp là: {0}/{1}/{2}".format(d+1, m, y))
        else:
            print("Ngày không hợp lệ!")
    if m == 2:
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            if d == 29:
                print("Ngày kế tiếp là: {0}/{1}/{2}".format(1, m + 1, y))
            elif d < 29:
                print("Ngày kế tiếp là: {0}/{1}/{2}".format(d + 1, m, y))
            else:
                print("Ngày không hợp lệ!")
        else:
            if d == 28:
                print("Ngày kế tiếp là: {0}/{1}/{2}".format(1, m + 1, y))
            elif d < 28:
                print("Ngày kế tiếp là: {0}/{1}/{2}".format(d + 1, m, y))
            else:
                print("Ngày không hợp lệ!")
else:
    print("Ngày tháng năm không hợp lệ !!!")
"""
EXERCISE 5: Nhập vào 2 giá trị a, b và phép toán +, -, *, / . 
            Hãy xuất kq theo đúng phép toán đã nhập.
"""
print("*"*15,"EX5","*"*15)
print("Chương trình nhập phép toán cho 2 số")
a=float(input("Nhập số a: "))
b=float(input("Nhập số b: "))
tt=input("Nhập toán tử: ")
print("Phép toán là:",a,tt,b)
"""
EXERCISE 6: Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm.
"""
print("*"*15,"EX6","*"*15)
print("Chương trình nhập tháng xuất ra tháng đó thuộc quý mấy trong năm")
month=int(input("Nhập tháng: "))
if month > 0 and month < 13:
    if month in (1,2,3):
        print("Tháng", month, "thuộc Quý 1")
    elif month in (4,5,6):
        print("Tháng", month, "thuộc Quý 2")
    elif month in (7,8,9):
        print("Tháng", month, "thuộc Quý 3")
    else:
        print("Tháng", month, "thuộc Quý 4")
else:
    print("Số tháng không hợp lệ!!!")
