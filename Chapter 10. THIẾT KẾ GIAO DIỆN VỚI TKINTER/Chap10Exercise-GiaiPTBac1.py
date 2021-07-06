"""
EXERCISE: Giải phương trình bậc 1: ax + b = 0
"""
from tkinter import *
# function
def SolvedPTB1():
    hsa = float(a.get())
    hsb = float(b.get())
    if hsa == 0 and hsb == 0:
        c.set("PT Có Vô Số Nghiệm")
    elif hsa == 0 and hsb != 0:
        c.set("PT Vô Nghiệm")
    else:
        c.set("x = " + str(-hsb/hsa))

def Continue():
    a.set("")
    b.set("")
    c.set("")

# Init
root=Tk()
a=StringVar()
b=StringVar()
c=StringVar()
root.title("Giải phương trình bậc 1")
root.resizable(width=True,height=True)
root.minsize(width=300,height=400)

# Body
Label(root,text="PHƯƠNG TRÌNH BẬC 1",justify=CENTER).grid(row=0,columnspan=2)
Label(root,text="Hệ số a: ").grid(row=1,column=0)
Entry(root,width=30,textvariable=a).grid(row=1,column=1)

Label(root,text="Hệ số b: ").grid(row=2,column=0)
Entry(root,width=30,textvariable=b).grid(row=2,column=1)

frameBtn=Frame()
Button(frameBtn,text="Giải",command=SolvedPTB1).pack(side=LEFT)
Button(frameBtn,text="Tiếp tục",command=Continue).pack(side=LEFT)
Button(frameBtn,text="Thoát",command=root.quit).pack(side=LEFT)
frameBtn.grid(row=3,columnspan=2)

Label(root,text="Kết quả: ").grid(row=4,column=0)
Entry(root,width=30,textvariable=c).grid(row=4,column=1)

# Show GUI
root.mainloop()