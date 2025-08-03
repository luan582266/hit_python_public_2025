n1 = int(input('Số lượng sv đki ở bàn 1: '))
A = set()
for i in range(n1):
    a = input(f"Mã sinh viên thứ {i+1} tại bàn 1: ")
    A.add(a)
     
n2 = int(input('Số lượng sv dki ở bàn 2 là: '))
B = set()
for i in range(n2):
    b = input(f"Mã sinh viên thứ {i+1} ở bàn 2 là: ")
    B.add(b)
    
print("Các mã sinh viên ở bàn 1 là: ", A)
print("Các mã sinh viên ở bàn 2 là: ", B)

both = set()
for sv in A: 
    if sv in B:
        both.add(sv)
        
if both:
    print("Có sinh viên đki tại cả 2 bàn", both)
else: 
    print("Không có sinh viên đki tại cả 2 bàn")
    
all = set()
for i in A:
    all.add(i)
for i in B:
    all.add(i)
print("Số lượng sinh viên đki tại cả 2 bàn: ", all)

only = set()
for i in A:
    if i not in B:
        only.add(i)
print("Danh sách sinh viên đã đki lầ: ", only)