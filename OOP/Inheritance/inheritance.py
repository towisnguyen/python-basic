"""
SUMMARY:
- kế thừa thuộc tính
- kế thừa phương thức
"""


class Animal:
    stt = 1 
    def __init__(self,p_name,p_loai,p_keu):
        self.name = p_name
        self.type = p_loai
        self.talk = p_keu
        self.stt = Animal.stt
        Animal.stt += 1

    def Speak(self):
        print(self.talk)

    def Intro(self):
        print("Tôi là: " + self.name)
        print("Giống: " + self.type)
        print("Ngôn ngữ: " + self.talk)

#inheritance
class Dog(Animal):
    def __init__(self, p_name, p_loai, p_keu,p_schan):
        super().__init__(p_name, p_loai, p_keu)
        self.leg = p_schan

    def Speak(self):
        return "Gâu gâu .."

    def Intro(self):
        super().Intro()
        print("Số chân: " + self.leg)

#inheritance
class Chicken(Animal):
    def __init__(self, p_name, p_loai, p_keu,p_schan):
        super().__init__(p_name, p_loai, p_keu)
        self.leg = p_schan

    def Speak(self):
        return "Ò ó o .."

    def Intro(self):
        super().Intro()
        print("Số chân: " + self.leg)
        

cho = Dog("Cà Lem","Alaska","ss","4")
ga = Chicken("Gà chọi","Đông Tảo","gg","2")
cho.Intro()
ga.Intro()
print(cho.Speak())
print(ga.Speak())