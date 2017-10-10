print("введите число")
a = int(input())
b = 2
while a > 1:
	if a % b == 0:
		print(b)
		while a % b == 0:
			a /= b
	b += 1