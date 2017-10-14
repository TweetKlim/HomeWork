def arithmetic(a, b, proc):
	if proc == '+':
		return a + b
	elif proc == '-':
		return a - b
	elif proc == '*':
		return a * b
	elif proc == '/':
		return a // b
	else:
		return 'неизвестная операция'
		
a = int(input())
b = int(input())
proc = input()
print(arithmetic(a, b, proc))