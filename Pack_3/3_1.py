class Klas:
	def prov(str):
		a = True
		b = []
		for i in range(0,len(str)):
			if(str[i] == '[' or str[i] == '{' or str[i] == '('):
				b.append(str[i])
			elif(str[i] == ']' and b[len(b)-1] == '['):
				b.pop()
			elif(str[i] == '}' and b[len(b)-1] == '{'):
				b.pop()
			elif(str[i] == ')' and b[len(b)-1] == '('):
				b.pop()
			else:
				a = False
		if len(b) > 0:
			a = False
		return a
		
str = input()
a = Klas
print(a.prov(str))