"""
EXERCISE 1: Cho biết bn dấu * được in ra trên màn hình:
                a=0
                while a < 100:
                    print('*',end='')
                print()
**SOLVE:
        có 100 dấu * đc in ra
"""
# print("*"*15,"EX1","*"*15)
# sao=0
# while sao < 100:
#     print('*',end='')
#     sao+=1
# print()
# print("có ",sao,"dấu sao")
import math

"""
EXERCISE 2: Cho biết bn dấu * được in ra trên màn hình:
                a=0
                while a < 100:
                    b=0
                    while b < 40:
                        if (a+b) % 2 == 0:
                            print('*',end='')
                        b+=1
                    print()
                    a+=1
**SOLVE:
        có 2000 dấu * đc in ra
"""
# print("*"*15,"EX2","*"*15)
# a=0
# while a < 100:
#     b=0
#     while b < 40:
#         if (a+b) % 2 == 0:
#             print('*',end='')
#         b+=1
#     print()
#     a+=1
# print("có 2000 dấu sao")
"""
EXERCISE 3: Giải thích cách chạy các dòng lệnh range:
a. range(5)         --> từ 0 đến 4, step = 1
b. range(5,10)      --> từ 5 đến 9, step = 1
c. range(5,20,3)    --> từ 5 đến 17, step = 3
d. range(20,5,-1)   --> từ 20 về 6, step = -1
e. range(20,5,-3)   --> từ 20 về 8, step = -3
f. range(10,5)      --> không ra số
g. range(0)         --> không ra số
h. range(10,101,10) --> từ 10 đến 100, step = 10
i. range(10,-1,-1)  --> từ 10 về 0, step = -1
j. range(-3,4)      --> từ -3 đến 3, step = 1
k. range(0,10,1)    --> từ 0 đến 9, step = 1
"""
# print("*"*15,"EX3","*"*15)
# for i in range(10,-1,-1):
#     print(i,end=' ')

"""
EXERCISE 4: Cho biết bn dấu * được in ra trên màn hình:
                for a in range(20,100,5):
                    print('*',end='')
                print()
**SOLVE:
        Có 16 dấu sao
"""
# print("*"*15,"EX4","*"*15)
# dem=0
# for a in range(20,100,5):
#     print('*',end='')
#     dem+=1
# print()
# print("Có", dem,"dấu sao")
"""
EXERCISE 5: Viết lại code dưới đây bằng cách dùng từ khóa break thay thế cho biến done:
                done = False
                n,m = 0, 100
                while not done and n != m:
                    n = int(input())
                    if n < 0:
                        done = True
                    print("n =", n)
"""
# print("*"*15,"EX5","*"*15)
# n,m=0,100
# while n != m:
#     n = int(input())
#     if n < 0:
#         break
#     print("n =", n)
"""
EXERCISE 6: Vẽ các hình dưới đây:
    * * * *                 *                   *
    *     *               * *                   * *
    *     *             * * *                   *   *
    * * * *           * * * *                   * * * * * * *
                                                        *   *
                                                          * * 
                                                            *
"""
print("*"*15,"EX6","*"*15)
n=int(input("Nhập N: "))
print("Hình vuông")
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == 0 or i == n - 1:
            print("* ",end='')
        else:
            print('',end='  ')
    print()
print("Hình tam giác")
for i in range(n):
    # thêm khoảng trống vào ô tam giác vuông ngược
    for j in range(n - 1 - i):
        print('',end='  ')
    # vẽ tam giác vuông sau khi xoay 180 độ
    for j in range(i + 1):
        print('* ',end='')
    print()
print("Hai tam giác tương phản")
mid=(n//2) + 1
for i in range(n):
    # vẽ tam giác ở nữa trên
    for j in range(mid):
        if i == mid - 1 or i == j or (j == 0 and i < mid):
            print('* ',end='')
        else:
            print('',end='  ')
    # vẽ tam giác ở nữa dưới
    for j in range(mid,n):
        if i == mid - 1 or i == j or (j == n - 1 and i >= mid):
            print('* ',end='')
        else:
            print('',end='  ')
    print()
"""
EXERCISE 7: Tính S(x,n) = x + x^3/3! + x^5/5! + ... + x^(2n+1)/(2n+1)!
"""
# print("*"*15,"EX7","*"*15)
# print("Tính S(x,n) = x + x^3/3! + x^5/5! + ... + x^(2n+1)/(2n+1)!")
# x=int(input("Nhập x: "))
# n=int(input("Nhập n: "))
# s=0
# for i in range(1,n+1):
#     if i % 2 != 0:
#         tu=x**i
#         mau=math.factorial(i)
#         s+=tu/mau
# print("S({0}, {1}) = {2}".format(x,n,s))