s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhâp chuỗi s2: ")

print("Chuỗi s1 sau khi đảo ngược là: ", s1[::-1])

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

if 1 <= a < b <= len(s2):
    reversed_sub = s2[a-1:b][::-1]
    new_s2 = s2[:a-1] + reversed_sub + s2[b:]
    print("Chuỗi s2 sau khi đảo ngược đoạn từ vị trí", a, "đến", b, ":", new_s2)
else:
    print("Giá trị a, b không hợp lệ!")

s3 = ""
for i in range(len(s1)):
    if i % 2 != 0:
        s3 += s1[i]
print("Chuỗi s3 sau khi xóa đi các phần tử chẵn là: ", s3)

s4 = ""
for i in range(min(len(s1), len(s2))):
    s4 += s1[i] + s2[i]
s4 += s1[i+1:] + s2[i+1:]
print("Chuỗi s4 sau khi đan xen ký tự của s1 và s2 là: ", s4)