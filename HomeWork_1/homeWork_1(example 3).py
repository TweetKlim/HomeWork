print("введите число")
a = int(input())
b = 2
while b + 1 < a:
	if a % b == 0:
		print('не простое')
		break
	b += 1
else:
	print('простое')