"""
EXERCISE: Nhập vào 1 năm bất kỳ, kiểm tra năm đó có phải năm nhuần hay không.
          Biết rằng: Năm nhuần là năm chia hết cho 4 nhưng không chia hết cho 100 hoặc chia hết cho 400
**SOLVE:
    y % 4 == 0 and y % 100 != 0 or y % 400 == 0
"""
y=int(input("Nhập một năm bất kì: "))
print("Là năm nhuần" if (y % 4 == 0 and y % 100 !=0) or y % 400 == 0 else "Năm không nhuần")