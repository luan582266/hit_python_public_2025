a = [1, 2, 3, 4, 5]
for x in range(len(a)):
    if x < 4:
        print(a[x], end = " ")
    else: 
        print(a[x], sep = " \n", end = " ")
# copy list 
a = [1, 2, 3, 4]
b = a * 2
print(b)
c = [0]
d = c * 100
print(len(d))
# đếm số lượng phần tử 
e = [1, 2, 2, 3, 3, 4, 5]
print(e.count(2))
pos = e.index(3)
print(pos)
# sắp xếp theo thứ tự giảm dần
e.sort(reverse = True)
print(e)
n = int(input())
arr = []

for i in range(n):
    x = int(input())
    arr.append(x)
    print(arr)
a = [1, 2, 3, 4, 5]
b = [x for x in a if x % 2 == 1]
print(b)
f = ["Hello", "World", "Python"]
g = sorted(f, key = lambda x : len(x))
print(g)