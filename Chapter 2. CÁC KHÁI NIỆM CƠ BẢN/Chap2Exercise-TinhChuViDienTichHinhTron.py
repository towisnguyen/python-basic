"""
EXERCISE: Nhập bán kính đường tròn r. Tính và Xuất chu vi, diện tích đường tròn tương ứng
**SOLVE:
    cv=2*pi*r và dt=pi*r*r
"""
import math
try:
    r=float(input("Nhập bán kính đường tròn: "))
    cv=2*math.pi*r
    dt=math.pi*r*r
    print("Chu vi = {0} và Diện tích = {1}".format(cv,dt))
except:
    print("Bị lỗi rồi!")
