"""
EXERCISE:   Cho một tập tin có dữ liệu trên mỗi dòng như dưới đây:
            5,6,8,9,-5
            -9,5,4,7,8
            6,7,8,3,6,46,7,2,-6,-7
            1. Viết hàm đọc file, mỗi dòng khởi tạo thành 1 list và xuất ra màn hình
            2. Xuất các số âm trên mỗi dòng ra màn hình
"""
print("Chương trình xử lý dữ liệu chuỗi số")
from FileRWSLib import *

def XuatSoAm(lstSP):
    for row in lstSP:
        for element in row:
            if int(element) < 0:
                print(element,end='\t')
        print()
    print()

dscs=ReadFile('DSChuoiSo.txt',",")
print("1. Danh sách các chuỗi số: ")
XuatSP(dscs)
print("2. Các số âm trong danh sách: ")
XuatSoAm(dscs)