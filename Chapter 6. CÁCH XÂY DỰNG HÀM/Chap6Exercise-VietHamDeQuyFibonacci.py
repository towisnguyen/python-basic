"""
EXERCISE:   Dãy số Fibonacci có dạng:
            1 -> 1 -> 2 -> 3 -> 5 -> 8 -> 13 -> 21 -> ...
            Được định nghĩa theo công thức đệ qui như dưới đây:
                Nêu n = 1, n = 2 -> Fn = 1
                n>2 Fn = F(n-1) + F(n-2)
            Viết 2 hàm:
            - Hàm trả về số Fib tại vị trí thứ n bất kỳ
            - Hàm trả về danh sách dãy số Fib từ 1 tới n
"""
def Fibonacci(n):
    if n <= 2:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)

def listFibonacci(n):
    for i in range(1,n+1):
        print(Fibonacci(i), end='\t')

print("Chương trình tính dãy số Fibonacci(n).")
n=int(input("Nhập n: "))
fib=Fibonacci(n)
print("Dãy Fibonacci({0}) = {1}".format(n,fib))
listFibonacci(n)