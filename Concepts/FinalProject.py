from tkinter import *
"""
EXERCISE 1:     Viết phần mềm Quản Lý Sản Phẩm
                - Mỗi danh mục có: Mã, tên; Một danh mục có nhiều sp
                - Mỗi sản phẩm có: Mã, tên, đơn giá; Mỗi sp thuộc về 1 danh mục
                - Cho phép: Lưu mới, sửa, xóa, tìm kiếm, sắp xếp, lưu và đọc Text File
"""
# Function
# Body
"""
EXERCISE 2:     Viết phần mềm Quản Lý Sinh Viên
                - Mỗi lớp có: Mã lớp, tên; một lớp có nhiều SV
                - Mỗi SV có: mã, tên, năm sinh; Mỗi SV thuộc về 1 lớp
                - Cho phép: Lưu mới, sửa, xóa, tìm kiếm, sắp xếp, lưu và đọc Text File
"""
# Function
# Body
"""
EXERCISE 3: Viết phần mềm Quản Lý Sách:
            - gồm mã sách, tên sách, năm xuất bản
            - Cho phép: Thêm, sửa, xóa, tìm kiếm, sắp xếp, lưu và đọc Text File
"""
# Function
lstSP=[]
count=0
def insertSP():
    global lstSP
    global count
    ma=maSP.get()
    ten=tenSP.get()
    nam=namXB.get()
    lb.insert(1,str(ma+ten+nam))
def editSP():
    pass
def deleteSP():
    pass
def searchSP():
    pass
def sortSP():
    pass
# Body
root=Tk()
maSP=StringVar()
tenSP=StringVar()
namXB=StringVar()
root.title("Quản Lý Sản Phẩm")
root.resizable(width=True,height=True)
root.minsize(width=500,height=700)

Label(root,text="Quản lý Sản Phẩm").pack(side=TOP)
lb=Listbox(root,width=80).pack(side=TOP)

frameInput1=Frame()
Label(root,text="Mã sách:").pack(side=TOP)
Entry(root,textvariable=maSP).pack(side=TOP)
Label(root,text="Tên sách:").pack(side=TOP)
Entry(root,textvariable=tenSP).pack(side=TOP)
Label(root,text="Năm xuất bản:").pack(side=TOP)
Entry(root,textvariable=namXB).pack(side=TOP)
frameInput1.pack()

frameBtn=Frame()
Button(frameBtn,text="Thêm",command=insertSP).pack(side=LEFT)
Button(frameBtn,text="Sửa",command=editSP).pack(side=LEFT)
Button(frameBtn,text="Xóa",command=deleteSP).pack(side=LEFT)
Button(frameBtn,text="Tìm kiếm",command=searchSP).pack(side=LEFT)
Button(frameBtn,text="Sắp xếp",command=sortSP).pack(side=LEFT)
frameBtn.pack()

root.mainloop()