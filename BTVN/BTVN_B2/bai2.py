luong = float(input("Nhập lương của bạn (đơn vị triệu đồng): "))
if luong <= 7: 
    thue = luong * 0.1
elif 7 < luong <= 15: 
    thue = luong * 0.2
else: 
    thue = luong * 0.3
luong_rong = luong - thue
print("Lương thực của nhân viên là: ", luong_rong, "triệu đồng")