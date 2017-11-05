s = input()
t = 0
p = ''
otvet = ''
znak = ''
for i in range(len(s)):
	p = ''
	y = ''
	if (s[i] == 'x'):
		for g in range(i - t):
			p += s[g+t]
		if (i + 1 < len(s)):
			if(s[i+1] == '^' or s[i+1] != '+' or s[i+1] != '-' ):
				q = i+1
				while((s[q] != '+' and s[q] != '-')and q < len(s)-1):
					q+=1
					if(s[q] != '+' and s[q] != '-'): y += s[q]
				t = q
		if (len(p) == 0): x1 = 1
		else: x1 = float(p)
		if (len(y) == 0): x2 = 1
		else: x2 = float(y)
		x12 = x1*x2
		if(int(x12) == x12): x12 = int(x12)
		if(int(x2) == x2): x2 = int(x2)
		if(x2 >= 1):
			if(len(znak) == 1):otvet += znak
			if(x12 > 1 or x2 == 1):otvet += str(x12)
			if(x2 != 1):otvet += 'x'
			if(x2-1 > 1):
				otvet +='^'
				otvet +=str(x2-1)
		znak = s[q]
print(otvet)
				