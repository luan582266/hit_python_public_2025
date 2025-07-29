n = int(input("Nhập số nguyên n: "))

dem = 0
tong = 0

while n > 0: 
    a = n % 10
    dem += 1
    tong += a
    n //= 10
    
print("Số lượng chữ số là: ", dem)
print("Tổng các chữ số là: ", tong)