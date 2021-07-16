"""
EXERCISE:   Một chuỗi được gọi là tối ưu khi không chứa các khoảng trắng dư thừa, các từ cách nhau bởi 1 khoảng trắng
**SOLVE:
"""
print("Chương trình tối ưu một chuỗi")
def toiUuChuoi(s):
    """
    Hàm tối ưu chuỗi, Một chuỗi được gọi là tối ưu khi không chứa các khoảng trắng dư thừa,
    các từ cách nhau bởi 1 khoảng trắng
    :param s: input chuỗi chưa được tối ưu
    :return: trả về chuỗi đã tối ưu
    """
    s2=s
    s2=s.strip()
    arr=s2.split(' ')
    s2=""
    for x in arr:
        word=x
        if len(word.strip())!=0:
            s2=s2+word+" "
    return s2.strip()

s="  trần   duy    hưng    "
print(s," => ",len(s))
s=toiUuChuoi(s)
print(s," => ",len(s))