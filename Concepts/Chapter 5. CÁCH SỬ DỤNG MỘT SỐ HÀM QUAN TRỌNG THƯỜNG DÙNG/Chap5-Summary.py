"""
CÁC HÀM TOÁN HỌC THƯỜNG DÙNG
-----------------------
from math import *
x,y=5,7
print(pow(x,y))                 # x^y
print(sqrt(25))                 # căn bậc 2 của 5
print(radians(30))              # đổi đơn vị độ sang radian
print(degrees(radians(30)))     # chuyển đơn vị radian về độ
print(log10(100))               # logarit cơ số 10 của 100

# Hàm lượng giác
sin(radians(góc))
cos(radians(góc))
tan(radians(góc))

# round func
round(number,digit) -> làm tròn số number với digit chữ số
                       hàm round không làm thay đổi giá trị số gốc mà nó trả về só mới đc làm tròn

#Time
## Clock func --> tùy vào hệ điều hành mà clock tính theo đơn vị khác nhau. Tính bằng giây nếu hđh là WINDOWN
from time import clock
print("Enter your name: ", end='')
start_time = clock()
name = input()
elapsed = clock() - start_time
print(name,"it took you", elapsed, "seconds to respond")

## Sleep func
for x in range(10):
    print(x)
    sleep(1) # xuất x sau 1 giây

# Random func
randrange(x,y) --> lấy số ngẫy nhiên từ >= x và < y

# Exit func
exit() --> hàm thoát phần mềm
ví dụ:
    while True:
        s=input("Nhập số: ")
        dem=0
        for i in range(1,n+1):
            if n % i == 0:
                dem+=1
        if (dem==2):
            print(s,"là số nguyên tố")
        else:
            print(s,"không phải số nguyên tố")
        print("Tiếp không ? (y/n)")
        if input() == "k":
            exit()
    print("BYE!")

# Eval func
eval() --> có thể tự tính toán chuỗi phép toán
ví dụ:
    from math import sin
    x = eval("1+2+5+sin(30)")
    print(x)

"""
from math import sqrt, log
from random import randrange
from time import sleep

"""
EXERCISE 1: Những giá trị nào dưới đây có thể xuất hiện khi chạy randrange(0,100)??
            4.5, 34, -1, 100, 0, 99
**SOLVE: số 34,0,99 có thể xuất hiện
"""
# print("*"*15,"EX1","*"*15)
# print(randrange(0,100))
"""
EXERCISE 2: Nhập tọa độ 2 điểm A(xA,yA), B(xB,yB). Tính và xuất độ dài đoạn AB.
                |AB|=dAB=sqrt(((xB-xA)**2)+((yB-yA)**2))
**SOLVE:
"""
# print("*"*15,"EX2","*"*15)
# xA,yA=eval(input("Nhập tọa độ điểm A(xA,yA): "))
# xB,yB=eval(input("Nhập tọa độ điểm B(xB,yB): "))
# print("Tọa độ 2 điểm là: A({0}, {1}), B({2}, {3})".format(xA,yA,xB,yB))
# print("Độ dài AB = ",sqrt(((xB-xA)**2)+((yB-yA)**2)))
"""
EXERCISE 3: Viết chương trình tính loga(x) với a,x là các số thực nhập vào từ bàn phím
            và x>0, a>0, a!=1
**SOLVE: dùng logax = lnx/lna
"""
# print("*"*15,"EX3","*"*15)
# print("Chương trình tính Loga(x)")
# a=float(input("Nhập cơ số a: "))
# x=float(input("Nhập x: "))
# if x>0 and a>0 and a!=1:
#     print("Log({0}){1} = {2}".format(a,x,log(x)/log(a)))
# else:
#     print("a,x phải là số thực và luôn dương, a khác 1!!!")
"""
EXERCISE 4: Nhập n. Tính S(n)=sqrt(2+sqrt(2+sqrt(2+sqrt(2+...+sqrt(2))))), có n dấu căn lồng nhau
**SOLVE: 
"""
# print("*"*15,"EX4","*"*15)
# s=0
# n=int(input("Nhập số dấu căn n: "))
# for i in range(n):
#     s=sqrt(2+s)
# print("S({0}) = {1}".format(n, s))
"""
EXERCISE 5: Vẽ 4 hình dưới đây, dùng sleep để xuất hiện từng hình sau 5 giây

              *                   *                     * * * *                * * * *
              * *                 * *                   * * *                  *   *
              * * *               *   *                 * *                    * *
        * * * * * * *       * * * * * * *               *                      *
        * * *               *   *                     * *                    * *
        * *                 * *                     * * *                  *   *
        *                   *                     * * * *                * * * *
"""
print("*"*15,"EX5","*"*15)
n=7
print("Hình 1")
mid=(n//2)

#sleep(5)
print("Hình 2")
#sleep(5)
print("Hình 3")
for i in range(n, mid, -1):
    for j in range(i):
        print("i,j: ",i,j)
        if j>=mid:
            print("* ", end="")
        else:
            print("",end="  ")
    print()

#sleep(5)
print("Hình 4")