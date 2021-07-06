"""
EXERCISE:   Viết chương trình cho phép:
            - Khởi tạo và nhập vào ma trận MxN phần tử ngẫu nhiên
            - Xuất dòng bất kỳ nhập từ bàn phím
            - Xuất cột bất kì nhập từ bàn phím
            - Xuất số max trong ma trận
"""
from random import randrange

print("Chương trình Xử lý list đa chiều")
m=int(input("Nhập số dòng: "))
n=int(input("Nhập số cột: "))
matrix=[]
for i in range(m):
    row=[]
    for j in range(n):
        row.append(randrange(-100,100))
    matrix.append(row)
print("1. Ma trận ",m,"x",n,": ")
print("- Xuất ma trận theo collection: ")
for row in matrix:
    for col in row:
        print("{:>4}".format(col),end='\t')
    print()
print("- Xuất ma trận theo index: ")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print("{:>4}".format(matrix[i][j]),end=' ')
    print()
print("2. Xuất dòng bất kỳ")
dong=int(input("Nhập dòng số: "))
lstRow=matrix[dong]
for element in lstRow:
    print(element,end='\t')
print("\n3. Xuất cột bất kỳ")
cot=int(input("Nhập cột số: "))
listCol=[]
for i in range(len(matrix)):
    listCol.append(matrix[i][cot])
for elem in listCol:
    print(elem,end='\t')
print("\n4. Xuất số max trong ma trận")
def MaxInMatrix(matrix):
    max=matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(max<matrix[i][j]):
                max=matrix[i][j]
    return max
print("Số lớn nhất trong ma trận: ",MaxInMatrix(matrix))