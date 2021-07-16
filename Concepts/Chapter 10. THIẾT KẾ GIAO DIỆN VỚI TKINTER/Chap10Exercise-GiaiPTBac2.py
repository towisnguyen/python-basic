"""
EXERCISE: Giải phương trình bậc 2: ax^2 + bx + c = 0
"""
from math import sqrt
from tkinter import *
def Continue():
    hsa.set("")
    hsb.set("")
    hsc.set("")
    kq.set("")
def SolvedPTB2():
    a=float(hsa.get())
    b=float(hsb.get())
    c=float(hsc.get())
    if a == 0:
        # bx + c = 0
        if b == 0 and c == 0:
            kq.set("PT có vô số nghiệm")
        elif b == 0 and c != 0:
            kq.set("PT vô nghiệm")
        else:
            kq.set("x = " + str(-c / b))
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            kq.set("PT vô nghiệm")
        elif delta == 0:
            kq.set("x1 = x2 = " + str(-b / (2 * a)))
        else:
            kq.set("x1 = " + str((-b - sqrt(delta)) / (2 * a)))
            kq.set("x2 = " + str((-b + sqrt(delta)) / (2 * a)))

#Init
root=Tk()
hsa=StringVar()
hsb=StringVar()
hsc=StringVar()
kq=StringVar()
root.title("Giải PT Bậc 2")
root.resizable(width=True,height=True)
root.minsize(width=300,height=400)
# Body
Label(root,text="PHƯƠNG TRÌNH BẬC 2",justify=CENTER,font=16,fg='red').grid(row=0,columnspan=2)
Label(root,text="Hệ số a: ").grid(row=1,column=0)
Entry(root,width=30,textvariable=hsa).grid(row=1,column=1)

Label(root,text="Hệ số b: ").grid(row=2,column=0)
Entry(root,width=30,textvariable=hsb).grid(row=2,column=1)

Label(root,text="Hệ số c: ").grid(row=3,column=0)
Entry(root,width=30,textvariable=hsc).grid(row=3,column=1)

frameBtn=Frame()
Button(frameBtn,text="Giải",command=SolvedPTB2).pack(side=LEFT)
Button(frameBtn,text="Tiếp tục",command=Continue).pack(side=LEFT)
Button(frameBtn,text="Thoát",command=root.quit).pack(side=LEFT)
frameBtn.grid(row=4,columnspan=2)

Label(root,text="Kết quả: ").grid(row=5,column=0)
Entry(root,width=30,textvariable=kq).grid(row=5,column=1)

# Show GUI
root.mainloop()