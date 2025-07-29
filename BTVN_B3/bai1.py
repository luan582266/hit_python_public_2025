n = int(input('n = '))
a = []
for i in range(n):
    a.append(int(input("Nhập phần tử thứ {i}: ")))
    print(a)
x = int(input('Nhập số nguyên cần kiểm tra: '))
print('Số lần x xuất hiện trong list là: ', a.count(x))
a[2 : 7] = [8, 5, 4, 0, 1, 3]
print(a)
print(max(a))
print(min(a))
y = int(input('Nhập số cần chèn: '))
a[:0] = [y]
print(a)
if a == sorted(a):
    print("Tăng")
elif a == sorted(a, reverse = True ):
    print("Giảm")
else: 
    print("NO")