"""
EXERCISE: Xuất bản cửu chương từ 1 -> 10
"""
print("Bảng cửu chương")
for i in range(1,11):
    for j in range(1,11):
        line="{0}*{1:>2}={2:>2} ".format(j,i,i*j)
        print(line,end='\t')
    print()