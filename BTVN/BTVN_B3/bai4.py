ten = input("Nhập họ tên chưa chuẩn hóa: ")

ds_tu = ten.strip().split()

ds_tu_chuan = []
for tu in ds_tu:
    tu_moi = tu.lower().capitalize()  
    ds_tu_chuan.append(tu_moi)

ten_chuan = " ".join(ds_tu_chuan)

print("Họ tên chuẩn hóa là:", ten_chuan)
