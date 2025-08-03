set1 = {1, 2, 3.1, 2, 'python', 'python'}
print(set1)
print(type(set1))
#các phần tử trung nhau khi in chỉ xuất hiện 1 lần 
list1 = [1, 2, 4, 5, 4]
set2 = set(list1)
print(set2)

string1 = "CLB HIT" 
set3 = set(string1)
print(set3)
#set ko in ra theo thứ tụ mình code mà nó in ra theo thứ tự ô nhớ của set 
d = {1, 2, 3, 4, 6, 4, 8, 3}
f = set(d)
f.pop()
print(f)
e = {4, 5, 6}
e.clear()
print(e)
print()

a = {1, 2, 3}
for x in a:
    print(x, end = " ")
print()

c = {'hello', 'python'}
c.discard('hello')
print(c)

c.discard(5)
print(c)
#xóa đi phần tử không có trong set vẫn không báo lỗi, bỏ qua phần tử đó và chạy tiếp tối ưa hơn remove()
print()
a = set()
for i in range(10):
    a.add(i)
print(a)
print()

set1 = {'toi', 'yeu'}
set2 = {'HIT', 'toi'}

result = set1.union(set2)
print(result)
print()

result = set1.intersection(set2)
print(result)
print()

result1 = set1.difference(set2)
result2 = set2.difference(set1)
print(result1)
print(result2)
print()

result = set1.symmetric_difference(set2)
print(result)
print()

result = set2.isdisjoint(set1)
print(result)
print()
#check set1 và set2 có phần tử nào chung không 
result = set1.issubset(set2)
print(result)
print()
#check set1 có phải set con của set2  không và ngược lại 
tuple1 = (1, 2, 'python', (1, 2))
print(tuple1)
print(type(tuple1))
print()

list1 = [1, 2, [1, 2, 3]]
tuple2 = tuple(list1)
print(tuple2)
print()
a = (1, 2, 3, 'python')
print(a[0])
print(a[0:3])
a, b, c, d = a
print(a, b, c, d, sep = ", ")
print()
a = (2, 3, 4, 5, 7, 8)
#for each
for x in a: 
    print(x, end = ' ')
print()
#for 
for i in range(len(a)):
    print(a[i], end = ' ')
print()

a1 = ('hit', 'python', 'public')
a2 = (1, 2, '2025')
print()

c = (10, 8, 7, 5)
c_sort = tuple(sorted(c))
print(c_sort)
print()

a = (1, 2, 3, 4, 5, 3, 1, 1, 2)
print(a.count(1))
#trả về ví trị của phần tử chỉ định
print(a.index(2))