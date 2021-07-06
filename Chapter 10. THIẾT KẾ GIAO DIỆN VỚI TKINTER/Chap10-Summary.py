"""
https://www.geeksforgeeks.org/python-tkinter-tutorial/
from tkinter import *
# khởi tạo
root=Tk()
root.title("First Project!")
Label(root,text="Hello World!").pack(pady=10)
Button(root,text="BOOM!",command=root.quit).pack()
e=StringVar()
Entry(root,textvariable=e,width=30).pack()
e.set("NHT")
# Show GUI
root.mainloop()
"""
import calendar
from tkinter import *
# Init
root=Tk()
"""
EXERCISE 3:     Thiết kế calculator đơn giản
"""
# # Function
# expression=""
# def press(num):
#     global expression
#     expression = expression + str(num)
#     equation.set(expression)
#
# def clear():
#     global expression
#     expression=""
#     equation.set("")
#
# def equal():
#     try:
#         global expression
#         total = str(eval(expression))
#         equation.set(total)
#         expression=""
#     except:
#         expression=""
#         equation.set(0)
# # Body
# equation=StringVar()
# root.title("Calculator")
# root.resizable(width=True,height=True)
# root.minsize(width=300,height=400)
#
# Entry(root,textvariable=equation,width=30).grid(row=0,columnspan=4)
#
# frameBtn1=Frame()
# Button(frameBtn1,text=" 1 ",width=5,command=lambda :press(1)).pack(side=TOP,fill=X)
# Button(frameBtn1,text=" 4 ",width=5,command=lambda :press(4)).pack(side=TOP,fill=X)
# Button(frameBtn1,text=" 7 ",width=5,command=lambda :press(7)).pack(side=TOP,fill=X)
# Button(frameBtn1,text=" . ",width=5,command=lambda :press(".")).pack(side=TOP,fill=X)
# frameBtn1.grid(row=1,column=0,rowspan=4)
#
#
# frameBtn2=Frame()
# Button(frameBtn2,text=" 2 ",width=5,command=lambda :press(2)).pack(side=TOP,fill=X)
# Button(frameBtn2,text=" 5 ",width=5,command=lambda :press(5)).pack(side=TOP,fill=X)
# Button(frameBtn2,text=" 8 ",width=5,command=lambda :press(8)).pack(side=TOP,fill=X)
# Button(frameBtn2,text=" 0 ",width=5,command=lambda :press(0)).pack(side=TOP,fill=X)
# frameBtn2.grid(row=1,column=1,rowspan=4)
#
# frameBtn3=Frame()
# Button(frameBtn3,text=" 3 ",width=5,command=lambda :press(3)).pack(side=TOP,fill=X)
# Button(frameBtn3,text=" 6 ",width=5,command=lambda :press(6)).pack(side=TOP,fill=X)
# Button(frameBtn3,text=" 9 ",width=5,command=lambda :press(9)).pack(side=TOP,fill=X)
# Button(frameBtn3,text=" . ",width=5,command=lambda :press(".")).pack(side=TOP,fill=X)
# frameBtn3.grid(row=1,column=2,rowspan=4)
#
# frameBtn4=Frame()
# Button(frameBtn4,text=" + ",width=5,command=lambda :press("+")).pack(side=TOP,fill=X)
# Button(frameBtn4,text=" - ",width=5,command=lambda :press("-")).pack(side=TOP,fill=X)
# Button(frameBtn4,text=" x ",width=5,command=lambda :press("*")).pack(side=TOP,fill=X)
# Button(frameBtn4,text=" / ",width=5,command=lambda :press("/")).pack(side=TOP,fill=X)
# frameBtn4.grid(row=1,column=3,rowspan=4)
#
# Button(root,text=" Clear ",width=18,command=clear).grid(row=5,columnspan=3)
# Button(root,text=" = ",width=5,command=equal).grid(row=5,column=3)

"""
EXERCISE 4:     Thiết kế màn hình đăng nhập
"""
# # Function
# def SignUp():
#     usrName=usr.get()
#     passWord=pasw.get()
#     print("Username: " + usrName + " và Password: " + passWord)
# # Body
# usr=StringVar()
# pasw=StringVar()
# root.title("Sign up")
# root.resizable(width=True,height=True)
# root.minsize(width=300,height=400)
#
# Label(root,text="Đăng Nhập",justify=CENTER).grid(row=0,columnspan=2)
#
# Label(root,text="Username:").grid(row=1,column=0)
# Entry(root,textvariable=usr,width=30).grid(row=1,column=1)
#
# Label(root,text="Password:").grid(row=2,column=0)
# Entry(root,textvariable=pasw,width=30,show='*').grid(row=2,column=1)
#
# Button(root,text="Đăng nhập",justify=CENTER,command=SignUp).grid(row=3,column=1)

"""
EXERCISE 5:     Thiết kế màn hình chuyển năm Dương Lịch (1982) thành Âm Lịch (Nhâm tuất)
** SOLVED: (Số năm – 3 )/ 12 lấy số dư tìm theo bảng địa chi của năm (12 con giáp)
Bảng Thiên Can
Số dư chia cho 10 Thiên Can
1 Giáp
2 Ất
3 Bính
4 Đinh
5 Mậu
6 Kỷ
7 Canh
8 Tân
9 Nhâm
0 Quý

Bảng Địa Chi
Số dư chia cho 12 Địa Chí
1 Tý
2 Sửu
3 Dần
4 Mão
5 Thìn
6 Tị
7 Ngọ
8 Mùi
9 Thân
10 Dậu
11 Tuất
0 Hợi

Ví dụ người sinh năm 1947 Blog Hồn Quê Hà Duy Tự Tính tuổi theo âm lịch: (1947 – 3 )/ 10 dư 4 . Tra bảng thiên can là Đinh
(1947 – 3 )/ 12 dư 0. Tra bảng địa chi được Hợi. Vậy sinh năm 1947 là tuổi Đinh Hợi
"""
# # Function
# showYear=""
# def ChangeYear():
#     try:
#         global showYear
#         y = int(yDuong.get())
#         # Bảng Thiên Can
#         if (y-3)%10 == 1:
#             showYear += "Giáp"
#         elif (y-3)%10 == 2:
#             showYear += "Ất"
#         elif (y-3)%10 == 3:
#             showYear += "Bính"
#         elif (y - 3) % 10 == 4:
#             showYear += "Đinh"
#         elif (y-3)%10 == 5:
#             showYear += "Mậu"
#         elif (y-3)%10 == 6:
#             showYear += "Kỷ"
#         elif (y-3)%10 == 7:
#             showYear += "Canh"
#         elif (y-3)%10 == 8:
#             showYear += "Tân"
#         elif (y-3)%10 == 9:
#             showYear += "Nhâm"
#         else:
#             showYear += "Quý"
#
#         # Bảng Địa Chi
#         if (y-3)%12 == 1:
#             showYear += " Tý"
#         elif (y-3)%12 == 2:
#             showYear += " Sửu"
#         elif (y-3)%12 == 3:
#             showYear += " Dần"
#         elif (y - 3) % 12 == 4:
#             showYear += " Mẹo"
#         elif (y-3)%12 == 5:
#             showYear += " Thìn"
#         elif (y-3)%12 == 6:
#             showYear += " Tị"
#         elif (y-3)%12 == 7:
#             showYear += " Ngọ"
#         elif (y-3)%12 == 8:
#             showYear += " Mùi"
#         elif (y-3)%12 == 9:
#             showYear += " Thân"
#         elif (y-3)%12 == 10:
#             showYear += " Dậu"
#         elif (y-3)%12 == 11:
#             showYear += " Tuất"
#         else:
#             showYear += " Hợi"
#
#         yAm.set(showYear)
#         showYear = ""
#     except:
#         showYear=""
#         yAm.set("error!")
# def showCalendar():
#     guiCal=Tk()
#     guiCal.config(background="white")
#     guiCal.title("CALENDER")
#     guiCal.resizable(width=True,height=True)
#     guiCal.minsize(width=700,height=800)
#     year=int(yDuong.get())
#     cal_content=calendar.calendar(year)
#     Label(guiCal,text=cal_content,font="Consolas 10 bold").grid(row=5,column=1)
#     guiCal.mainloop()
# # Body
# yDuong=StringVar()
# yAm=StringVar()
# root.title("Đổi năm Dương Lịch sang năm Âm Lịch")
# root.resizable(width=True,height=True)
# root.minsize(width=300,height=400)
# Label(root,text="Đổi năm Dương Lịch -> Âm Lịch",font=16,fg='red',justify=CENTER).grid(row=0,columnspan=5)
# Label(root,text="Năm Dương",justify=CENTER).grid(row=1,column=0)
# Entry(root,textvariable=yDuong,width=10).grid(row=2,column=0)
#
# Button(root,text="Change",justify=CENTER,command=ChangeYear).grid(row=2,column=2)
#
# Label(root,text="Năm Âm",justify=CENTER).grid(row=1,column=4)
# Entry(root,textvariable=yAm,width=10).grid(row=2,column=4)
#
# Button(root,text="Calendar",justify=CENTER,command=showCalendar).grid(row=3,column=2)

"""
EXERCISE 6:     Thiết kế màn hình chuyển độ F sang độ C
** SOLVED:  Độ C = (5*(độ F -32))/9
            Độ F = (9*độ C/5) + 32
"""
# # Function
# def ChangeDegreeFToC():
#     f=float(doF.get())
#     c=(5*(f-32))/9
#     doC.set(str(round(c)))
# # Body
# doF=StringVar()
# doC=StringVar()
# root.title("Đổi độ F sang độ C")
# root.resizable(width=True,height=True)
# root.minsize(width=300,height=400)
# Label(root,text="Độ F -> Độ C",font=16,fg='red',justify=CENTER).grid(row=0,columnspan=5)
# Label(root,text="Độ F",justify=CENTER).grid(row=1,column=0)
# Entry(root,textvariable=doF,width=10).grid(row=2,column=0)
#
# Button(root,text="Change",justify=CENTER,command=ChangeDegreeFToC).grid(row=2,column=2)
#
# Label(root,text="Độ C",justify=CENTER).grid(row=1,column=4)
# Entry(root,textvariable=doC,width=10).grid(row=2,column=4)
"""
EXERCISE 7:     Thiết kế màn hình tính BMI
"""
# # Function
# def BMI():
#     height=float(h.get())
#     weight=float(w.get())
#     csbmi=weight/((height/100)**2)
#     bmi.set(str(csbmi))
#     if (csbmi<18.5):
#         ploai.set("Gầy")
#         ncbenh.set("Ít")
#     elif csbmi <= 24.9:
#         ploai.set("Bình thường")
#         ncbenh.set("Trung bình")
#     elif csbmi <= 29.9:
#         ploai.set("Béo")
#         ncbenh.set("Béo phì, đái tháo đường ...")
#     elif csbmi <= 34.9:
#         ploai.set("Béo phì cấp độ 1")
#         ncbenh.set("Cao, cần giảm cân và ăn uống khoa học")
#     elif csbmi <= 39.9:
#         ploai.set("Béo phì cấp độ 2")
#         ncbenh.set("RẤT CAO, cần tập thể dục và đến trung tâm y tế để khám")
#     else:
#         ploai.set("Béo phì cấp độ 3")
#         ncbenh.set("NGUY HIỂM đến tính mạng, bạn nên đến bệnh viện để chữa trị")
# # Body
# w=StringVar()
# h=StringVar()
# bmi=StringVar()
# ploai=StringVar()
# ncbenh=StringVar()
#
#
# root.title("BMI")
# root.resizable(width=True,height=True)
# root.minsize(width=300,height=400)
#
# Label(root,text="Chỉ Số BMI",font=16,fg='red',justify=CENTER).grid(row=0,columnspan=2)
# Label(root,text="Nhập cân nặng (kg): ").grid(row=1,column=0)
# Entry(root,textvariable=w).grid(row=1,column=1)
#
# Label(root,text="Nhập chiều cao (cm): ").grid(row=2,column=0)
# Entry(root,textvariable=h).grid(row=2,column=1)
#
# Button(root,text="Tính BMI",justify=CENTER,command=BMI).grid(row=3,column=1)
#
# Label(root,text="Chỉ số BMI của bạn: ").grid(row=4,column=0)
# Entry(root,textvariable=bmi).grid(row=4,column=1)
#
# Label(root,text="Phân loại: ").grid(row=5,column=0)
# Entry(root,textvariable=ploai).grid(row=5,column=1)
#
# Label(root,text="Nguy cơ bệnh: ").grid(row=6,column=0)
# Entry(root,textvariable=ncbenh).grid(row=6,column=1)

# Show GUI
root.mainloop()