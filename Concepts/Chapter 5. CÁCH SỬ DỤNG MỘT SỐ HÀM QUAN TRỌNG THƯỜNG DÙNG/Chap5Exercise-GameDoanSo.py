"""
EXERCISE:   Máy ra 1 số trong đoạn [1...100]
            Người chơi đoán số, chỉ đc phép đoán sai 7 lần. Mỗi lần đoán sẽ thông báo số người chơi đoán
            nhỏ hơn hay lớn hơn số của máy và hiển thị số lần đoán.
            Game kết thúc khi đoán sai quá 7 lần hoặc đoán trúng trước 7 lần
            Sau khi game kết thúc hỏi người chơi có tiếp tục hay không?
**SOLVE:
"""
from math import *
from random import randrange

while True:
    somay=randrange(1,101)
    solandoan=0
    win=False
    while solandoan<7:
        solandoan+=1
        songuoi=int(input("Máy ra số [1...100], mời bạn đoán số: "))
        print("Lần đoán thứ", solandoan)
        if somay==songuoi:
            print("Chúc mừng bạn đã đoán đúng, số máy là ",somay)
            win=True
            break
        if somay > songuoi:
            print("Bạn đã đoán sai, số máy > số bạn đoán !")
        elif somay < songuoi:
            print("Bạn đã đoán sai, số máy < số bạn đoán !")
    if win==False:
        print("GAME OVER!!!, số máy là ",somay)
    ask = input("Tiếp tục? (y/n)")
    if ask=="n":
        break
print("Cảm ơn bạn đã chơi game, Hẹn gặp lại!!!")