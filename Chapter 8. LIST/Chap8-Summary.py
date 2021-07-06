"""
CÁC HÀM THƯỜNG DÙNG LIST
-----------------------------------------
1. Duyệt list: - theo collection -> print(x,end='\t') for x in lst:
            - theo index -> print(lst[i],end='\t') for x in range(len(lst)):
2. Function:
    insert(vị trí chèn, giá trị chèn): chèn  vào vị trí thích hợp
    append(giá trị chèn): chèn giá trị vào cuối list
    remove(giá trị): xóa giá trị trong list hoặc dùng hàm del lst[0]
    reverse(): đảo ngược list gốc ,ngoài ra còn có hàm reserved(lst) trả về list mới
    sort(): sắp xếp list gốc tăng dần or giảm dần dùng lst.sort(reverse=True),
            ngoài ra còn có hàm sorted(lst) trả về list mới
    list[begin:end:step]: dùng để trích lọc list
3. Duyệt List đa chiều:
        matrix = [
                    [100, 14, 8 , 22],
                    [0, 243, 68, 1],
                    [90, 21, 7, 67]
                 ]
        print(matrix)
        # cách duyệt theo collection
        for row in matrix:  # duyệt từng dòng
            for elem in row: # lấy từng phần từ trên mỗi dòng
                print('{:>4}'.format(elem),end='\t')
            print()

        #duyệt theo index
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], end='\t')
            print()

"""
import random

"""
EXERCISE 1:     Cho list: lst = [3, 0, 1, 5, 2]
                          x = 2
                Hãy cho biết kết quả:
                a. lst[0] = 3                        e. lst[x+1] = 5
                b. lst[3] = 5                        f. lst[x] + 1 = 2
                c. lst[x] = 1                        g. lst[lst[x]] = 0
                d. lst[-x] = 5                       h. lst[lst[lst[x]]] = 3
**SOLVE:
"""
# print("*"*15,"EX1","*"*15)
# lst = [3, 0, 1, 5, 2]
# x = 2
# print("a->d: ",lst[0],lst[3],lst[x],lst[-x],end='\n')
# print("\ne->h: ",lst[x+1],lst[x] + 1,lst[lst[x]],lst[lst[lst[x]]],end='\n')
"""
EXERCISE 2:     Cho list: lst = [20, 1, -34, 40, -8, 60, 1, 3]
                Hãy cho biết kết quả:
a. lst=[20, 1, -34, 40, -8, 60, 1, 3]  e. lst[-5:-3]=[40, -8]                   i. lst[:4]=[20, 1, -34, 40] m. len(lst)=8
b. lst[0:3]=[20, 1, -34]               f. lst[-22:3]=[3,1,60,-8,40]             j. lst[1:5]=[1, -34, 40, -8]
c. lst[4:8]=[-8, 60, 1, 3]             g. lst[4:]=[-8, 60, 1, 3]                k. -34 in lst = True
d. lst[4:33]=[-8, 60, 1, 3]            h. lst[:]=[20, 1, -34, 40, -8, 60, 1, 3] l. -34 not in lst = False
**SOLVE:
"""
# print("*"*15,"EX2","*"*15)
# lst = [20, 1, -34, 40, -8, 60, 1, 3]
# print("a -> d: ",lst,lst[0:3],lst[4:8],lst[4:33],end="\n")
# print("e -> h: ",lst[-5:-3],lst[-22:3],lst[4:],lst[:],end="\n")
# print("i -> m: ",lst[:4],lst[1:5],-34 in lst,-34 not in lst,len(lst),end="\n")
"""
EXERCISE 3:     Nhập vào 1 list có N số ngẫu nhiên KHÔNG TRÙNG NHAU
**SOLVE:
"""
# print("*"*15,"EX3","*"*15)
# n=int(input("Nhập số phần tử N = "))
# lst=list(range(-n,n))
# random.shuffle(lst)
# lst1=[]
# for i in range(n):
#     lst1.append(lst[i])
# print(lst1)

"""
EXERCISE 4:     Viết chương trình nhập vào một dãy các số theo thứ tự tăng, nếu nhập sai cách thì yêu cầu nhập lại.
                In dãy số sau khi nhập xong
**SOLVE:
"""
# print("*"*15,"EX4","*"*15)
# lsz=int(input("Nhập chiều dài dãy số: "))
# lst=[]
# for i in range(lsz):
#     n=int(input("Nhập số theo thứ tự tăng dần: "))
#     lst.append(n)
#     if lst[i-1] >= n and i > 1:
#         i-=1
#         lst.remove(lst[i - 1])
#
# print("Dãy số là : ",lst)
"""
EXERCISE 5:     Viết chương trình nhập vào 1 dãy n số hực M[0], ..., M[n-1], sắp xếp dãy số theo thứ tự giảm dần.
                Xuất ra dãy số sau khi sắp xếp
**SOLVE:
"""
# print("*"*15,"EX5","*"*15)
# n=int(input("Số lượng phần tử N = "))
# lstF=[]
# for i in range(n):
#     m=float(input("Nhập phần tử: "))
#     lstF.append(m)
# print(lstF)
# print("Day số sau khi sắp xếp: ",sorted(lstF,reverse=True))
"""
EXERCISE 6:     Viết chương trình nhập vào 1 mảng số tự nhiên. Hãy xuất ra màn hình
                - Dòng 1: gồm các số lẻ, tổng cộng có bao nhiêu số lẻ
                - Dòng 2: gồm các số chẵn, tổng cộng có bao nhiêu số chẵn
                - Dòng 3: gồm các số nguyên tố
                - Dòng 4: gồm các số không phải là số nguyên tố
                M[] = {3,6,7,8,11,17,2,90,2,5,4,5,8}
                -> 3,7,11,17,5(2) -> 6 số lẻ
**SOLVE:
"""
# print("*"*15,"EX6","*"*15)
# def IsSnt(n):
#     count = 0
#     if n == 2 or n == 1:
#         return True
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#         return True
#     else:
#         return False
#
# n=int(input("Số lượng phần tử N = "))
# lstInt=[]
# for i in range(n):
#     m=int(input("Nhập phần tử: "))
#     lstInt.append(m)
# countLe=0
# lstLe=[]
# countChan=0
# lstChan=[]
# lstSnt=[]
# lstKSnt=[]
# for i in range(len(lstInt)):
#     if lstInt[i] % 2 != 0:
#         countLe+=1
#         lstLe.append(lstInt[i])
#     if lstInt[i] % 2 == 0:
#         countChan+=1
#         lstChan.append(lstInt[i])
#     if IsSnt(lstInt[i]):
#         lstSnt.append(lstInt[i])
#     if IsSnt(lstInt[i]) is False:
#         lstKSnt.append(lstInt[i])
# print("Dòng 1: Có ",countLe," số lẻ và dãy số lẻ ",lstLe)
# print("Dòng 2: Có ",countChan," số chẵn và dãy số chẵn: ",lstChan)
# print("Dòng 3: Dãy các số nguyên tố : ",lstSnt)
# print("Dòng 4: Dãy các số không phải là số nguyên tố : ",lstKSnt)
"""
EXERCISE 7:     Nhập 2 matrix A, B
                Cộng 2 matrix
                Viết hàm tính matrix hoán vị -> áp dụng để tìm ma trận hoán vị cho A,B 
**SOLVE:
"""
# print("*"*15,"EX7","*"*15)
