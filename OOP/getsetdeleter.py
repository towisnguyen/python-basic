class Account:
    def __init__(self,ho,ten):
        self.ho=ho
        self.ten=ten

    @property
    def hoten(self): #getter
        return "{} {}".format(self.ho,self.ten)
    @property
    def email(self): #getter
        return "{}-{}@gmail.com".format(self.ho,self.ten)
    
    @hoten.setter
    def hoten(self, nnew):
        ho, ten = nnew.split(' ')
        self.ho = ho
        self.ten = ten

    @hoten.deleter
    def hoten(self):
        self.ho = None
        self.ten = None
        print("Đã xóa")

print("----- Getter: ")
acc=Account("Nguyễn","Hồng Tới")
print(acc.ho)
print(acc.ten)
print(acc.hoten)
print(acc.email)
print("----- Setter: ")
acc.hoten = "Nguyễn Towis"
print(acc.hoten)
print(acc.email)
print("----- Deleter: ")
del acc.hoten
print(acc.hoten)