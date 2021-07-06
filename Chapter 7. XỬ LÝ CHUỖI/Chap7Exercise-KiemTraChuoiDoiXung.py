"""
EXERCISE:   Dùng vòng lặp while vĩnh cửu, cho phép Nhập vào 1 chuỗi -> xuất Chuỗi này có phải đối xứng không?
            Hỏi người dùng có tiếp tục phần mềm ? Nếu tiếp tục thì nhập Chuỗi mới, còn không thì thoát và cảm ơn.
**SOLVE:
        ví dụ: abcddcba là chuỗi đối xứng
"""
print("Chương trình kiểm tra chuỗi đối xứng")
def kiemTraDoiXung(s):
    """
    Hàm kiểm tra chuỗi có đối xứng hay không?
    :param s: input chuỗi
    :return: trả về True nếu chuỗi đối xứng, ngược lại là False
    """
    dx=True
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            dx=False
            break
    return dx

while True:
    s=input("Nhập chuỗi ký tự: ")
    if kiemTraDoiXung(s):
        print("Chuỗi đối xứng!!!")
    else:
        print("Chuỗi không đối xứng")
    ask=input("Tiếp tục sử dụng phần mềm?(y/n) ")
    if ask=="n":
        break
print("Cảm ơn đã sử dụng phần mềm!")