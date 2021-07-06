"""
SUMMARY: Các hàm thường sử dụng trong chuỗi
------------
=>>>>> object.methodname(parameter list) <<<<<<=
upper, lower: Xử lý in Hoa, in thường
rjust, ljust, center: Căn lề phải, căn lề trái, căn giữa
strip: xóa khoảng trắng dư thừa
startswith, endswith: kiểm tra Chuỗi có phải bắt đầu là ký tự ?, kết thúc là ký tự ?
count: đếm số lần xuất hiện trong chuỗi
find: Tìm kiếm chuỗi con
format: định dạng chuỗi
__len__(): trả về số lượng ký tự trong chuỗi, dùng index để lấy ký tự ra: str[index]
split: hàm tách chuỗi ban đầu thành 1 mảng con
join: hàm nối chuỗi
"""
import re

"""
EXERCISE 1:     Viết chương trình cho phép nhập vào 1 chuỗi. Yêu cầu xuất ra:
                - Bao nhiêu chữ IN HOA
                - Bao nhiêu chữ in thường
                - Bao nhiêu chữ là chữ số
                - Bao nhiêu chữ là ký tự đặc biệt
                - Bao nhiêu chữ là khoảng trắng
                - Bao nhiêu chữ là Nguyên Âm
                - Bao nhiêu chữ là Phụ âm
"""
# print("*"*15,"EX1","*"*15)
# print("Chương trình liệt kê chuỗi có bao nhiêu chữ IN HOA, in thường, chữ số, ký tự đặc biệt, khoảng trắng, Nguyên Âm, Phụ Âm")
# str="abc DEF gh IJKl mno PQ /*-+.,/' 123456  "
# inHoa=0
# inThuong=0
# chuSo=0
# kyTuDb=0
# khoangTrang=0
# nguyenAm=0
# phuAm=0
# for i in range(len(str)):
#     if str[i].isupper():
#         inHoa+=1
#     if str[i].islower():
#         inThuong+=1
#     if str[i].isnumeric():
#         chuSo+=1
#     if str[i].isspace():
#         khoangTrang+=1
#     if re.match("[-()\"#/@;:<>{}`'+=~|.!?,]", str[i]):
#         kyTuDb += 1
#     if str[i].lower() in 'aeiou':
#         nguyenAm+=1
#     if str[i].lower() in 'bcdfghjklmnpqrstvwxyz':
#         phuAm+=1
#
# print("Chuỗi: ", str)
# print("Có ", inHoa," chữ IN HOA")
# print("Có ", inThuong," chữ in thường")
# print("Có ", chuSo," chữ là chữ số")
# print("Có ", kyTuDb," chữ là ký tự đặc biệt")
# print("Có ", khoangTrang," chữ là khoảng trắng")
# print("Có ", nguyenAm," chữ là Nguyên Âm")
# print("Có ", phuAm," chữ là Phụ âm")
"""
EXERCISE 2:     Viết một hàm đặt tên là NegativeNumberInStrings(str). Hàm này có đối số truyền vào là một chuỗi bất kỳ.
                Hãy viết lệnh xuất ra các số nguyên âm trong chuỗi
                Ví dụ: Nếu nhập vào chuỗi "abc-5xyz-12k91--p" thì phải xuất ra đc 2 số nguyên âm là -5 và -12
**HINT:
def getNegatives(your_str):
    negatives=[]
    i=0
    while i+1<len(your_str):
        if all([your_str[i]=='-',your_str[i+1].isnumeric()]):
            negative=''
            while i+1<len(your_str) and your_str[i+1].isnumeric():
                negative+=your_str[i+1]
                i+=1
            else:
                negatives+=[-int(negative)]
        i+=1
    return negatives
"""
# print("*"*15,"EX2","*"*15)
# def NegativeNumberInStrings(str):
#     negative=[]
#     for i in range(len(str)):
#         if str[i] == '-' and str[i+1].isnumeric():
#             nega=''
#             while i + 1 < len(str) and str[i+1].isnumeric():
#                 nega+=str[i+1]
#                 i+=1
#             else:
#                 negative+=[-int(nega)]
#     return negative

# str="abc-5xyz-123k91--p"
# print("Số âm là: ",NegativeNumberInStrings(str))
"""
EXERCISE 3:     Viết chương trình tối ưu Chuỗi danh từ
                Ví dụ:
                input: "   NGuyễn hỒnG      TớI    "
                Output: "Nguyễn Hồng Tới"
"""
# print("*"*15,"EX3","*"*15)
# def ToiUuChuoi(s):
#     """
#         Hàm tối ưu chuỗi, Một chuỗi được gọi là tối ưu khi không chứa các khoảng trắng dư thừa,
#         các từ cách nhau bởi 1 khoảng trắng
#         :param s: input chuỗi chưa được tối ưu
#         :return: trả về chuỗi đã tối ưu
#     """
#     s2 = s
#     s2 = s.lower().strip()  # biến chuỗi thành chữ thường và bỏ khoảng trắng dư thừa
#     arr = s2.split(' ')     # tách chuỗi bằng khoảng trắng
#     s2 = ""
#     for x in arr:
#         word = x
#         # nếu từ được loại bỏ khoảng trắng dư thừa có kích thước khác 0 thì nối từ,
#         # hàm capitalize() để viết hoa chữ cái đầu của từ
#         if len(word.strip()) != 0:
#             s2 = s2 + word.capitalize() + " "
#     return s2.strip()
#
# s="   NGuyễn hỒnG      TớI    "
# print(s," => ",len(s))
# s=ToiUuChuoi(s)
# print(s," => ",len(s))
