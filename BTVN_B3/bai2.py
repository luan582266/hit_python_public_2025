# Nhập dữ liệu
a = list(map(int, input("Nhập list a: ").split()))
k = len(a)
n = int(input("Nhập số dòng n: "))
m = int(input("Nhập số cột m: "))

if k >= n * m:
    b = []
    for i in range(n):
        row = a[i * m : (i + 1) * m]
        b.append(row)
    
    for row in b:
        print(row)
else:
    print("NO")
