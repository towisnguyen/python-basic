"""
SUMMARY:
- __init__(self): hàm initial dùng làm constructor
"""


class Animal:
    stt = 1 
    def __init__(self,p_name,p_loai,p_keu):
        self.name = p_name
        self.type = p_loai
        self.talk = p_keu
        self.stt = Animal.stt
        Animal.stt += 1

    # regular method
    def Speak(self):
        print(self.talk)

    def Intro(self):
        print("Tôi là: " + self.name)
        print("Giống: " + self.type)
        print("Ngôn ngữ: " + self.talk)

cho = Animal("Cà lem","Alaska","Gaugaugau")
ga = Animal("Gà chiến","Đông Tảo","ò ó o o ..")

print(cho.Intro())
print(cho.stt)
print(ga.Intro())
print(ga.stt)
