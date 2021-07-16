"""
EXERCISE:   BMI là chỉ số cân đối cơ thể. Yêu cầu đầu ào nhập là chiều cao và cân nặng,
            hãy cho biết người này như thế nào, biết rằng:
            -------------------------------------------------------------------------------
            Chỉ số khối cơ thể              Phân loại              Nguy cơ phát triển bệnh
            -------------------------------------------------------------------------------
                < 18.5                          Gầy                       Thấp
                18.5 - 24.9                 Bình thường                   Trung bình
                25.0 - 29.9                 Hơi béo                       Cao
                30.0 - 34.9                 Béo phì cấp độ 1              Cao
                35.0 - 39.9                 Béo phì cấp độ 2              Rất cao
                > 40.0                      Béo phì cấp độ 3              Nguy hiểm
            --------------------------------------------------------------------------------
**SOLVE:
        BMI = Cân nặng (kg)/ chiều cao ** 2 (m)
"""
def BMI(h, w):
    """
    Hàm tính chỉ số BMI, là chỉ số cân đối cơ thể.
    Dựa vào chỉ số BMI để phân loại và cảnh báo nguy cơ cho người.
    :param h: input chiều cao tính theo đơn vị (cm)
    :param w: input cân nặng tính theo đơn vị (kg)
    :return: trả về chỉ số BMI
    """
    return w/((h/100)**2)
def phanLoai(bmi):
    """
    Hàm phân loại và cảnh báo nguy cơ có bệnh cho người dựa vào chỉ số BMI
    :param bmi: input chỉ số BMI
    :return: đưa ra phân loại và cảnh báo
    """
    if (bmi<18.5):
        print("Cơ thể của bạn khá gầy, hãy ăn đầy đủ và bổ sung nhiều vitamin nhé!")
    elif bmi <= 24.9:
        print("Cơ thể của bạn bình thường cân đối và ít có nguy cơ phát triển bệnh.")
    elif bmi <= 29.9:
        print("Cơ thể của bạn hơi béo, cần tập thể dục hoặc giảm khẩu phần ăn vì có nguy cơ phát triện bệnh như: béo phì, đái tháo đường ... ")
    elif bmi <= 34.9:
        print("Cơ thể của bạn đang ở mức béo phì cấp độ 1 và có nguy cơ phát triển bệnh cao, cần giảm cân và ăn uống khoa học!!!")
    elif bmi <= 39.9:
        print("Cơ thể của bạn đang ở mức béo phì cấp độ 2 và có nguy cơ phát triển bệnh RẤT CAO, cần tập thể dục và đến trung tâm y tế để khám")
    else:
        print("Cơ thể của bạn đang ở mức béo phì cấp độ 3, NGUY HIỂM đến tính mạng, bạn nên đến bệnh viện để chữa trị!!!")

print("Chương trình tính chỉ số BMI")
h=float(input("Nhập chiều cao của bạn: "))
w=float(input("Nhập cân nặng của bạn: "))
bmi=BMI(h,w)
print("Chỉ số BMI của bạn là: ",bmi)
phanLoai(bmi)