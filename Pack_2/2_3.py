import copy
n = int(input())
a = [1]
t = " "
print(t * (n+1), end="")
print(a[0])
for i in range(0,n):
	b = copy.deepcopy(a)
	b.append(1)
	print(t*(n-i), end="")
	for p in range(0,i):
		b[p+1] = a[p+1] + a[p]
		print(b[p],end = " ")
	print(b[i],end = " ")
	print(b[i+1])
	a = b