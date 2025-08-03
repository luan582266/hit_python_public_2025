n = int(input("Nhập số lượng phần tử của tuple:"))

a = []

for i in range(n):
    b = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(b)

c = tuple(a)
tbc = sum(c) / len(c)
print("Tuple vừa nhập là: ", c)
print("Trung bình cộng các phần tử trong tuple là: ", tbc)