"""
EXERCISE:   Cho 1 chuỗi sau: "5;7;8;-2;8;11;13;9;10"
            - xuất các chữ số trên các dòng riêng biệt
            - xuất có bao nhiêu chữ số chẵn
            - Xuất có bao nhiêu số âm
            - xuất có bao nhiêu chữ số nguyên tố
            - tính giá trị trung bình
**SOLVE:
"""
print("Chương trình xử lý chuỗi")
def LaSoNguyenTo(n):
    count=0
    if n == 2 or n == 1:
        return True
    for i in range(1,n+1):
        if n % i == 0:
            count+=1
    if count==2:
        return True
    else:
        return False
def LaSoChan(f,n):
    return f(n)
def LaSoAm(f,n):
    return f(n)

s="5;7;8;-2;8;11;13;9;10"
arr=s.split(';')
print("các số trên các dòng riêng biệt: ")
countC=0
countA=0
countSnt=0
sumtb=0
for i in range(len(arr)):
    print(arr[i])
    if LaSoChan(lambda n:n%2==0, int(arr[i])):
        countC+=1
    if LaSoAm(lambda n:n<0, int(arr[i])):
        countA+=1
    if LaSoNguyenTo(int(arr[i])):
        countSnt+=1
    sumtb += int(arr[i])
    sumtb /= len(arr)
print("Có ",countC," chữ số chẵn")
print("Có ",countA," chữ số âm")
print("Có ",countSnt," chữ số nguyên tố")
print("Giá trị trung bình = ",sumtb)