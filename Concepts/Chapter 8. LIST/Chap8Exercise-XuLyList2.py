"""
EXERCISE:   Viết chương trình cho phép:
            - Viết lệnh khởi tạo ngẫu nhiên n phần tử cho list
            - Gọi k là 1 số nhập từ bàn phím, xóa tất cả các phần tử có giá trị k tồn tại trong list
            - Kiểm tra list có đối xứng hay không
"""
from random import randrange

print("Chương trình xử lý list")
print("1. Khởi tạo list ngẫu nhiên với n phần tử")
n=int(input("Nhập số phần tử n: "))
lst=[0]*n
for i in range(len(lst)):
    lst[i]=randrange(-100,100)
print(lst)
print("2. Xóa tất cả các phần tử có giá trị k tồn tại trong list")
k=int(input("Nhập số k: "))
while lst.count(k)>0:
    lst.remove(k)
print("List sau khi xóa", k,"\nlst = ",lst)
print("3. Kiểm tra list có đối xứng không")
flag=False
for i in range(len(lst)):
    if lst[i]==lst[len(lst) - 1 - i]:
        flag=True
if flag==True:
    print("Chuỗi đối xứng")
else:
    print("Chuỗi không đối xứng!!!")