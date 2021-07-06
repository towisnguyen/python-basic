"""
EXERCISE:   Viết chương trình cho phép:
            - Khởi tạo list
            - Thêm phần tử vào list
            - Nhập k, kiểm tra k xuất hiện bao nhiêu lần trong list
            - Tính tổng các số nguyên tố trong list
            - Sắp xếp
            - Xóa list
"""
from random import randrange
def KiemTraSoNguyenTo(n):
    count=0
    if n == 1 or n == 2:
        return 1
    for i in range(2,n):
        if n % i == 0:
            count +=1
    if count == 2:
        return True
    else:
        return False
def TongCacSoNguyenTo(list):
    s=0
    for i in range(len(list)):
        if KiemTraSoNguyenTo(list[i]):
            s+=list[i]
    return s
# def SoLanXuatHienK(k,list):
#     count=0
#     for i in range(len(list)):
#         if list[i]==k:
#             count+=1
#     return count

print("Chương trình Xử lý list")
print("1. Khởi tạo list và thêm phần tử vào list")
n=int(input("Nhập số phần tử: "))
lst=[0]*n
for i in range(len(lst)):
    lst[i]=randrange(-100,100)
print(lst)
val=int(input("Nhập thêm số mới: "))
lst.append(val)
print(lst)
print("2. Nhập k, kiểm tra k xuất hiện bao nhiêu lần trong list")
k=int(input("Nhập k: "))
dem=lst.count(k)
print(k," xuất hiện",dem," lần")
print("3. Tổng các số nguyên tố trong list")
print(TongCacSoNguyenTo(lst))
print("4. Sắp xếp")
lstSort1=sorted(lst)
lstSort2=sorted(lst,reverse=True)
print("List sắp xếp tăng dần: ",lstSort1)
print("List sắp xếp giảm dần: ",lstSort2)
print("5. Xóa list")
del lst
print("List đã xóa: ", lst)