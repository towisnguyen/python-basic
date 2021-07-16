"""
EXERCISE 1:     Cho 3 hàm dưới đây:
                def sum1(n):            def sum2():                 def sum3():
                    s=0                     global val                  s=0
                    while n>0:              s=0                         for i in range(val, 0, -1):
                        s+=1                while val > 0:                  s+=1
                        n-=1                    s+=1                    return s
                    return s                return s
                Hãy cho biết kết quả sau khi gọi các lên trên:
                def main():             def main():                 def main():
                    global val              global val                  global val
                    val = 5                 val = 5                     val = 5
                    print(sum1(5))          print(sum1(5))              print(sum2())
                    print(sum2())           print(sum3())               print(sum1(5))
                    print(sum3())           print(sum2())               print(sum3())
                main()                  main()                      main()
            --> s1=5, s2="lỗi", s3=0    --> s1=5, s3=5, s2=         --> "lỗi"
"""
# print("*"*15,"EX1","*"*15)
# def sum1(n):
#     s=0
#     while n > 0:
#         s+=1
#         n-=1
#     return s
# def sum2():
#     global val
#     s=0
#     while val > 0:
#         s+=1
#     return s
# def sum3():
#     s=0
#     for i in range(val, 0, -1):
#         s+=1
#     return s
# def main():
#     global val
#     val=5
#     print("s3= ", sum2())
#     print("s1= ",sum1(5))
#     print("s2= ",sum3())
#
# main()
"""
EXERCISE 2:     Cho coding:
                    for n in oscillate(-3, 5):
                        print(n, end=' ')
                    print()
                Hãy viết hàm oscillate để khi chạy phần mềm, nó ra kết quả:
                -3 3 -2 2 -1 1 0 0 1 -1 2 -2 3 -3 4 -4
"""
# print("*"*15,"EX2","*"*15)
# def oscillate(a,b):
#     for i in range(a,b):
#         print("{0} {1}".format(i,-i),end=' ')
#     print()
#
# for n in enumerate(oscillate(-3,5)):
#     print(n, end=' ')
# print()

"""
EXERCISE 3: Viết 1 hàm tính tổng ước số để áp dụng cho 2 bài dưới đây:
            3.1/ Kiểm tra số nguyên dương n có phải là số hoàn thiện hay không?
                 (số hoàn thiện là số có tổng các ước số của nó (không kể nó) thì bằng chính nó.
                  ví dụ: các ước số là 1, 2, 3 và 6 = 1 + 2 + 3 -> 6 là số hoàn thiện)
            3.2/ Kiểm tra số nguyên dương n có phải là số thình vượng hay không?
                 (số thịnh vượng là số có tổng các ước số của nó (không kể nó) thì lớn hơn nó.
                  ví dụ: 12 có các ước số là 1, 2, 3, 4, 6 và 12 < 1+2+3+4+6 -> 12 là số thịnh vượng)
"""
# print("*"*15,"EX3","*"*15)
# def tongUocSo(n):
#     """
#     Hàm tính tổng các ước số của một số
#     :param n: input số
#     :return: trả về tổng các ước số của số n
#     """
#     s=0
#     for i in range(1, n):
#         if n % i == 0:
#             s += i
#     return s
#
# def kiemTraSo(n):
#     if n == tongUocSo(n):
#         print(n, "là số hoàn thiện")
#     elif n < tongUocSo(n):
#         print(n, "là số thịnh vượng")
#     else:
#         print(n, "là số nguyên")
#
# kiemTraSo(7)