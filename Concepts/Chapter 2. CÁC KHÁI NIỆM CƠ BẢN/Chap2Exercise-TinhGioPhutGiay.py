"""
EXERCISE: Nhập vào số giây bất kì t. Tính và xuất ra dạng hh:mm:ss
ví dụ: nhập 3570 thì xuất ra 1:2:30 AM
       nhập 51100 thì xuất ra 2:11:40 PM
**SOLVE:
    hour = (t/3600)%24 -->
    minute = (t%3600)/60
    second = (t%3600)%60
"""
try:
    t=int(input("Nhập vào số giây bất kỳ: "))
    h=(t//3600)%24
    m=(t%3600)//60
    s=(t%3600)%60
    if h>12:
        print("Time zone: {0}:{1}:{2} PM".format(h - 12, m, s))
    else:
        print("Time zone: {0}:{1}:{2} AM".format(h, m, s))
except:
    print("Bị lỗi khi nhập đầu vào!!!")