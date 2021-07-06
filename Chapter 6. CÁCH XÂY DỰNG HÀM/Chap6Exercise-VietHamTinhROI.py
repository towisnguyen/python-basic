"""
EXERCISE:   ROI (Return On Investment) tạm dịch là tỷ lệ lợi nhuận thu được so với  chi phí bạn đầu tư.
            Có thể hiểu ROI một cách đơn giản chính là chỉ số đo lường tỷ lệ những gì bạn thu về so với những gì bạn bỏ ra

            Hiểu đúng bản chất của ROI, bạn sẽ đo lường hiệu quả đồng vốn đầu tư của mình cho các chi phí như
            quảng cáo, chạy Adwords, hay chi phí marketing online khác.

            Vì ROI dựa vào các chỉ số cụ thể, nên nó cũng là 1 thước đo rất cụ thể:
                ROI = (Doanh thu - Chi phí) / Chi phí

            Viết chương trình cho phép người dùng nhập vào Doanh thu và Chi phí và xuất ra tỉ lệ ROI cho người dùng
            , đồng thời hãy cho biết nên hay không nên đầu tư dự án khi biết ROI (giả sử mức tối thiểu ROI = 0.75 thì mới đầu tư)

"""
def ROI(dt,cp):
    """
    Hàm tính tỉ lệ ROI
    :param dt: input doanh thu
    :param cp: input chi phí
    :return: trả về tỉ lệ ROI
    """
    return (dt - cp)/cp
def IsInvest(roi):
    """
    Hàm gợi ý người dùng có nên đầu tư hay không dựa vào tỉ lệ ROI
    :param roi: input tỉ lệ ROI
    :return: trả về biến True = nên đầu tư, False = không nên
    """
    if roi >= 0.75:
        return "Nên đầu tư."
    else:
        return "Không nên đầu tư!!!"
print("Chương trình tính tỉ lệ ROI")
dt=float(input("Nhập doanh thu: "))
cp=float(input("Nhập chi phí: "))
roi=ROI(dt,cp)
print("Tỉ lệ ROI: ", roi)
print("Kết luận: ",IsInvest(roi))

