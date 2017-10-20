a = input()
b = len(a)
b //= 2
while b > 0:
	if a[b-1] != a[-b]:
		print('не полиндром')
		break;
	b -= 1
else:
	print('полиндром')