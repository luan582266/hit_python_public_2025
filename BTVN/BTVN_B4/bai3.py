n = int(input("Nhập n: "))
dem = 0
f = []
for i in range(n):
    a = input(f"Nhập phần tử thứ {i+1}: ")
    f.append(a)
print("Mang f sau khi nhập là: ", f)

m = int(input("Nhập m: "))
A = set()
for i in range(m):
    a = input(f"Nhập phần tử thứ {i+1}: ")
    A.add(a)
print("Set a sau khi nhập là: ", A)
B = set()
for i in range(m):
    b = input(f"Nhập phần tử thứ {i+1}: ")
    B.add(b)
print("Set B sau khi nhập là: ", B)

for i in f: 
    if i in A:
        dem += 1
    elif i in B:
        dem -= 1
    else: 
        dem += 0
print("Mức độ hạnh phúc cuối cùng là: ", dem)