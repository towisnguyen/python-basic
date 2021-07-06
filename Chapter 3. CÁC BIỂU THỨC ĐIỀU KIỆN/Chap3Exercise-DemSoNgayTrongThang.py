"""
EXERCISE: Nhập vào 1 tháng, xuất số ngày trong tháng đó.
          1,3,5,7,8,10,12 có 31 ngày
          4,6,9,11 có 30 ngày
          nếu tháng 2 yêu cầu nhập thêm năm. Năm nhuần thì có 29 ngày, không nhuần có 28 ngày
"""
try:
    x=int(input("Nhập 1 tháng bất kì: "))
    if x in (1,3,5,7,8,10,12):
        print("Tháng ",x," có 31 ngày")
    elif x in (4,6,9,11):
        print("Tháng ", x, " có 30 ngày")
    elif x == 2:
        y=int(input("Vui lòng nhập năm: "))
        if (y % 4 ==0 and y %100 !=0) and y%400==0:
            print("Năm", y, "nhuần nên Tháng ",x,"có 29 ngày")
        else:
            print("Năm", y, "không nhuần nên Tháng ", x, "có 28 ngày")
    else:
        print("Tháng không hợp lệ!!!")
except:
    print("Bị lỗi rồi!!!")