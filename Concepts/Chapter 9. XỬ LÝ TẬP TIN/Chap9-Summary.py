"""
CÁC HÀM GHI & ĐỌC TẬP TIN
--------------------------
1. Cách ghi tập tin:
open('myfile.txt','w') --> mở tập tin để ghi mới
open('myfile.txt','a') --> mở tập tin để ghi nối đuôi
Ví dụ:
def luuFile():
    f=open('csdlsv.txt','w',encoding='utf-8')
    f.writelines("sv01;Nguyễn Văn Chúc;9.5\n")
    f.writelines("sv02;Nguyễn Thị Mừng;8.5\n")
    f.writelines("sv01;Nguyễn Văn An;9.5\n")
    f.writelines("sv02;Nguyễn Thị Bê;8.5\n")
    f.close()
luuFile()
2. Cách đọc tập tin:
def docFile():
    f=open('csdlsv.txt','r',encoding='utf-8')
    for line in f:
        print(line.strip())
    f.close()
docFile()

"""
from random import randrange

"""
EXERCISE 1:     Trình bày kỹ thuật lưu file và đọc file trong Python
** SOLVED:
    Dùng phương thức open với 3 đối số:
    ví dụ: open('tên file','w/r/a',encoding='utf-8')
"""
print("*"*15,"EX1","*"*15)
"""
EXERCISE 2:     Viết phần mềm Quản Lý Sản Phẩm
                - Mỗi danh mục có: Mã, tên; Một danh mục có nhiều sp
                - Mỗi sản phẩm có: Mã, tên, đơn giá; Mỗi sp thuộc về 1 danh mục
                - Cho phép: Lưu mới, sửa, xóa, tìm kiếm, sắp xếp, lưu và đọc Text File
"""
# print("*"*15,"EX2","*"*15)
# print("Chương trình Quản Lý Sản Phẩm")
#
# while True:
#     print("-"*100)
#     print(" 1. Thêm      2. Sửa      3. Xóa      4. Tìm Kiếm     5. Sắp xếp      6.Lưu và đọc File    7. Thoát")
#     print("-"*100)
#     ask=int(input("Chọn 1 -> 7?: "))
#     if ask == 1:
#         # Thêm mới
#         pass
#     elif ask == 2:
#         # Sửa
#         pass
#     elif ask == 3:
#         # Xóa
#         pass
#     elif ask == 4:
#         # Tìm kiếm
#         pass
#     elif ask == 5:
#         # Sắp xếp
#         pass
#     elif ask == 6:
#         # Lưu và Đọc File
#         pass
#     elif ask == 7:
#         # Thoát
#         break

"""
EXERCISE 3:     Viết phần mềm Quản Lý Sinh Viên
                - Mỗi lớp có: Mã lớp, tên; một lớp có nhiều SV
                - Mỗi SV có: mã, tên, năm sinh; Mỗi SV thuộc về 1 lớp
                - Cho phép: Lưu mới, sửa, xóa, tìm kiếm, sắp xếp, lưu và đọc Text File
"""
# print("*"*15,"EX3","*"*15)
# print("Chương trình Quản Lý Sinh Viên")
"""
EXERCISE 4:     a. Viết hàm cho phép lưu tập tin dưới dạng text file, yêu cầu khởi tạo là 10 dòng,
                   Mỗi dòng có 10 số ngẫu nhiên cách nhau bởi dấu ";".
                b. Tiếp theo viết hàm cho phép đọc tập tin từ câu a, xuất ra tổng giá trị của các phần tử trên mỗi dòng
"""
# print("*"*15,"EX4","*"*15)
# def LuuRandom(path):
#     file = open(path,'a',encoding='utf-8')
#     for l in range(10):
#         for i in range(10):
#             file.write(str(randrange(-100,100)) + ';')
#         file.write('\n')
#     file.close()
#
# def ReadFile(path):
#     lstSP=[]
#     file=open(path,'r',encoding='utf-8')
#     for line in file:
#         data = line.strip()
#         lst = data.split(';')
#         lstSP.append(lst)
#     file.close()
#     return lstSP
#
# def XuatFile(lstSP):
#     for row in lstSP:
#         for element in row:
#             print(element,end='\t')
#             # print("{:>4}".format(element),end='\t')
#         print()
#     print()
#
# def XuatTongGiaTriTungLine(lstSP,nline):
#     s = 0
#     for j in range(len(lstSP)):
#         s+=int(lstSP[nline][j])
#     print(str(s))
#
#
# # LuuRandom('DSSoRandom.txt')
# dsrand=ReadFile('DSSoRandom.txt')
# print("Danh sách số random: ")
# XuatFile(dsrand)
# print("Tổng giá trị từng dòng: ")
# for i in range(10):
#     XuatTongGiaTriTungLine(dsrand,i)
