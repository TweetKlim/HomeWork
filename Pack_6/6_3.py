import lists

	
def find_V(V, L , len):
	n = L._header._next
	p = L._trailer._prev
	i = 0
	j = len
	while (n != p):
		if (n._element + p._element == V):
			return i ,j
		if (n._element + p._element > V):
			j -= 1
			p = p._prev
		if (n._element + p._element < V):
			i += 1
			n = n._next
	return None

L = lists.PositionalList()
list = input("L: ").split()
len = -1
for i in list:
	len += 1
	L.add_last(int(i))
V = int(input("V: "))

if (len > 0):
	resoult = find_V(V, L, len)
	if (resoult == None):
		print(None)
	else:
		print(resoult[0],resoult[1])
else:
	print("your list is empty")
