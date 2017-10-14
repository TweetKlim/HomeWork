import copy
n = int(input())
a = [1]
print(a)
for i in range(0,n):
	b = copy.deepcopy(a)
	b.append(1)
	for p in range(0,i):
		b[p+1] = a[p+1] + a[p]
	a = b
	print(a)
