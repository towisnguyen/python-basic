"""
EXERCISE:   Viết chương trình nhập vào thông tin của một SP:
            Mã: Chuỗi
            Tên: Chuỗi
            Đơn giá: Số
            Mỗi SP sau khi nhập thành công sẽ lưu nối đuôi vào File theo quy tắc:
            MSSP;Tên SP;Đơn giá
            - Xuất danh sách sản phẩm từ File
            - Sắp xếp SP theo đơn giá giảm dần
"""
print("Chương trình nhập vào thông tin của một Sản Phẩm")
from FileRWSLib import *
def SavedFile(path):
    file = open(path, 'a', encoding='utf-8')
    file.writelines(mssp + ';' + tensp + ';' + str(giasp) + '\n')
    file.close()

# while True:
#     mssp=input("Nhập mã SP: ")
#     tensp=input("Nhập tên SP: ")
#     giasp=float(input("Nhập đơn giá SP: "))
#     SavedFile('DSSP.txt')
#     tt=input("Thêm Sản Phẩm mới ? (y/n)")
#     if tt == 'n':
#         break

print("Danh sách sản phẩm: ")
dssp=ReadFile('DSSP.txt',';')
XuatSP(dssp)
print("Danh sách sản phẩm sau khi sắp xếp: ")
SortSP(dssp)
XuatSP(dssp)