"""
EXERCISE:   Nhập vào điểm toán lý hóa bằng chuỗi, theo thứ tự:
            Toán, lý, hóa = "7,4,6"
            Tính điểm trung bình lấy 2 chữ số lẻ thập phân
**SOLVE:
"""
t,l,h=eval(input("Nhập điểm toán, lý, hóa theo dạng (t,l,h): "))
print("Điểm trung bình = ",round((t+l+h)/3,2))