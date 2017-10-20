def function(a):
	с = 1
	b = 2 
	print(c)
	while a > 1:
		if a % b == 0:
			с += b
			while a % b == 0:
				a /= b
		b += 1
	return c
	
a = int(input())
if a == function(a) :
	print("замечательное")
else:
	print("не замечательное")