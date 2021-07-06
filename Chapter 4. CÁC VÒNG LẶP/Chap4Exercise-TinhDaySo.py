"""
EXERCISE: Tính S(x,n) = x + x^2/2! + x^3/3! + ... + x^n/n!
Ví dụ:
    S(2,3)=2 + 2^2/2! + 2^3/3! = 2 + 4/2 + 8/6 = 16/3
"""
import math

print("Tính dãy số: S(x,n) = x + x^2/2! + x^3/3! + ... + x^n/n!")
x=int(input("Nhập x: "))
n=int(input("Nhập n: "))
s=0
s1=0
for i in range(1,n+1):
    tu=x**i
    mau=1
    for j in range(1,i+1):
        mau=mau*j
    s = s + tu/mau
print("Op1: S({0}, {1}) = {2}".format(x,n,s))

for i in range(1,n+1):
    tu1=x**i
    mau1=math.factorial(i)
    s1 = s1 + tu1/mau1
print("Op2: S({0}, {1}) = {2}".format(x,n,s1))
