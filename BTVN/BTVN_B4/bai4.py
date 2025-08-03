n = int(input("Nhập kích thước mảng a: "))
a = []
for i in range(n):
    A = input(f"Nhập phần tử thứ {i+1} vào mảng: ")
    a.append(A)
print("Mảng a sau khi nhập là: ", a)

b = tuple(a)
print("Mảng b là: ", b)

dem = 0
for i in b: 
    if i.isdigit():  #kiểm tra nếu là chữ số thì in ra true ngược nếu có chữ thì in ra false
        dem += 1
print("Số phần tử có dạng số trong b là: ", dem)