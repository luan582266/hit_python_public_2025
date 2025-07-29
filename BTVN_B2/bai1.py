thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
if thang < 1 or thang > 12: 
    print("Tháng không hợp lệ")
elif thang == 2:
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print("Tháng có 29 ngày")
    else: 
        print("Tháng có 28 ngày")
elif thang in [4, 6, 9, 11]: 
    print("Tháng có 30 ngày")
else: 
    print("Tháng có 31 ngày")   
        