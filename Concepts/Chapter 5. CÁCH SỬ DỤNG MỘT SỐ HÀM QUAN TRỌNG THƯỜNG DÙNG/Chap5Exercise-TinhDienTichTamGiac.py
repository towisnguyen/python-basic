"""
EXERCISE:   Nhập vào 3 cạnh của tam giác, kiểm tra tính hợp lệ của tam giác.
            Sau đó tính diện tích theo công thức Herong:
                cv=a+b+c, p=cv/2 và dt=sqrt(p*(p-a)*(p-b)*(p-c))
**SOLVE:
"""
from math import sqrt

hople = False
while hople is False:
    a=float(input("Nhập cạnh thứ nhất của tam giác: "))
    b=float(input("Nhập cạnh thứ hai của tam giác: "))
    c=float(input("Nhập cạnh thứ ba của tam giác: "))
    if a+b>c and a+c>b and b+c>a and (a>0 or b>0 or c>0):
        hople = True
        print("Tam giác hợp lệ có 3 cạnh lần lượt ", a, b, c)
        cv=a+b+c
        p=cv/2
        dt=sqrt(p*(p-a)*(p-b)*(p-c))
        break
    else:
        print("Tam giác không hợp lệ, vui lòng nhập lại!!!")
        hople=False
print("Diện tích của tam giác = ", dt)