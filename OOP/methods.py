"""
SUMMARY:
- regular method
- class method dùng để cập nhật biến trong class
- static method
- special method để định nghĩa các toán tử như cộng chuỗi, cộng số, len chuỗi mong muốn...
"""

class Animal:
    power = 50
    def __init__(self,p_name,p_loai,p_keu):
        self.name = p_name
        self.type = p_loai
        self.talk = p_keu
        self.power = Animal.power
    
    # regular method
    def Speak(self):
        print(self.talk)

    def Intro(self):
        print("Tôi là: " + self.name)
        print("Giống: " + self.type)
        print("Ngôn ngữ: " + self.talk)

    @classmethod
    def update_power(cls,sm): #thường dùng tên hàm from_...()
        cls.power = sm
        return cls.power

    #special methos
    def __str__(self):
        return "Tôi là {0}, thuộc loại {1}, ngôn ngữ: {2}".format(self.name,self.type,self.talk)

    

cho = Animal("Ca lem","Alaska","Gaugaugau")

cho.Intro()
print(cho.__str__())
print(cho.power)
print(cho.update_power(40))