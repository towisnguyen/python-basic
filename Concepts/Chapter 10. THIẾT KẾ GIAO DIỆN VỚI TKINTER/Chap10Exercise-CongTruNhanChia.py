"""
EXERCISE:   Cộng trừ nhân chia 1 phép tính cho nhập hệ số a, b và trả về kết quả
"""
from tkinter import *
# Function
def Cong():
    hsa = float(a.get())
    hsb = float(b.get())
    kq.set(str(hsa+hsb))
def Tru():
    hsa = float(a.get())
    hsb = float(b.get())
    kq.set(str(hsa - hsb))
def Nhan():
    hsa = float(a.get())
    hsb = float(b.get())
    kq.set(str(hsa * hsb))
def Chia():
    hsa = float(a.get())
    hsb = float(b.get())
    kq.set(str(hsa / hsb))

# Init
root=Tk()
a=StringVar()
b=StringVar()
kq=StringVar()
root.title("Cộng trừ nhân chia cho phép tính")
root.resizable(width=True,height=True)
root.minsize(width=300,height=400)

# GUI opt $1
# Label(root,text="CỘNG TRỪ NHÂN CHIA PHÉP TÍNH",justify=CENTER).grid(row=0,columnspan=4)
#
# Button(root,text=" + ",width=5,command=Cong).grid(row=1,column=0)
# Label(root,text="Hệ số a: ").grid(row=1,column=2)
# Entry(root,width=10,textvariable=a).grid(row=1,column=3)
#
# Button(root,text=" - ",width=5,command=Tru).grid(row=2,column=0)
# Label(root,text="Hệ số b: ").grid(row=2,column=2)
# Entry(root,width=10,textvariable=b).grid(row=2,column=3)
#
# Button(root,text=" x ",width=5,command=Nhan).grid(row=3,column=0)
# Label(root,text="Kết quả: ").grid(row=3,column=2)
# Entry(root,width=10,textvariable=kq).grid(row=3,column=3)
#
# Button(root,text=" / ",width=5,command=Chia).grid(row=4,column=0)
# Button(root,text="Thoát",width=5,command=root.quit).grid(row=4,column=3)

# GUI opt $2

Label(root,text="CỘNG TRỪ NHÂN CHIA PHÉP TÍNH",justify=CENTER).grid(row=0,columnspan=3)
frameBtn=Frame()
Button(frameBtn,text=" + ",command=Cong).pack(side=TOP,fill=X)
Button(frameBtn,text=" - ",command=Tru).pack(side=TOP,fill=X)
Button(frameBtn,text=" * ",command=Nhan).pack(side=TOP,fill=X)
Button(frameBtn,text=" / ",command=Chia).pack(side=TOP,fill=X)
frameBtn.grid(row=1,column=0,rowspan=4)

Label(root,text="Hệ số a: ").grid(row=1,column=1)
Entry(root,width=10,textvariable=a).grid(row=1,column=2)
Label(root,text="Hệ số b: ").grid(row=2,column=1)
Entry(root,width=10,textvariable=b).grid(row=2,column=2)
Label(root,text="Kết quả: ").grid(row=3,column=1)
Entry(root,width=10,textvariable=kq).grid(row=3,column=2)
Button(root,text="Thoát",width=5,command=root.quit).grid(row=4,column=2)

#Show GUI
root.mainloop()