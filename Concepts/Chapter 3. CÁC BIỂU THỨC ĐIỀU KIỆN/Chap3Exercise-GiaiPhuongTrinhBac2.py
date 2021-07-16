"""
EXERCISE: Viết chương trình giải phương trình bậc 2: ax^2 + bx + c = 0
"""
from math import sqrt

print("Giải phương trình bậc 2: ax^2 + bx + c =0")
a=float(input("Nhập số a: "))
b=float(input("Nhập số b: "))
c= float(input("Nhập số c: "))
print("Phương trình bậc 2 có dạng: {0}x^2 + {1}x + {2} = 0".format(a,b,c))
if a == 0:
    #bx + c = 0
    if b == 0 and c ==0:
        print("PT có vô số nghiệm")
    elif b == 0 and c != 0:
        print("PT vô nghiệm")
    else:
        print("Nghiệm x = ",-c/b)
else:
    delta = b**2-4*a*c
    if delta<0:
        print("PT vô nghiệm")
    elif delta==0:
        print("Nghiệm kép x1=x2= ",-b/(2*a))
    else:
        print("Nghiệm x1 = ", (-b-sqrt(delta))/(2*a))
        print("Nghiệm x2 = ",(-b+sqrt(delta))/(2*a))