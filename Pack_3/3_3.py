def get_time(line):
    return int(line[0:2]) * 60 * 60 * 1000 + int(line[3:5]) * 60 * 1000 + int(line[6:8]) * 1000 + int(line[9:12])

def time(t):
	h = t // 3600000 
	m = (t - h *3600000) // 60000
	s = (t - h *3600000 - m * 60000) //1000
	ms = (t - h *3600000 - m * 60000 - s * 1000)
	return str(h) + ":" + str(m) + ":" + str(s) + ":" + str(ms)

class Cell():
	def __init__(self):
		self.s = list()
	def push(self, n):
		self.s.append(n)
	def pop(self):
		if len(self.s) > 0:
			self.s.pop(0)
	def front(self):
		if len(self.s) > 0:
			return self.s[0]
		else:
			return 0
	def empty(self):
		return len(self.s) == 0
	def size(self):
		return len(self.s)
	
left = 0			
d = {'V': None, 'D': None, 'X': None, 'Y': None, 'B': None, 'J': None, 'Q': None, 'Z': None, 'K': None, 'P': None, 'All': None}
mx = {'V': 0, 'D': 0, 'X': 0, 'Y': 0, 'B': 0, 'J': 0, 'Q': 0, 'Z': 0, 'K': 0, 'P': 0, 'All': 0}
mx_l = {'V': 0, 'D': 0, 'X': 0, 'Y': 0, 'B': 0, 'J': 0, 'Q': 0, 'Z': 0, 'K': 0, 'P': 0, 'All': 0}

f = open("TRD2.csv", "r")
a = f.readline()
for i in d:
	d[i] = Cell()
			
def input():
	a = f.readline()
	p = a.split(',')
	return p

def count():
	global left 
	f = False
	
	while True:
		s = input()
		if(s[0] == ''):
			return 0
		if not f:
			left = get_time(s[0])
			f = True
		t = get_time(s[0]) - left
		w =  d[s[3][0]].front()
		
		while t - w > 1000 and not d[s[3][0]].empty():
			w =  d[s[3][0]].front()
			d[s[3][0]].pop()
			
		d[s[3][0]].push(t)
		if mx[s[3][0]] < d[s[3][0]].size():		
			mx[s[3][0]] = d[s[3][0]].size()
			mx_l[s[3][0]] = d[s[3][0]].front()
		w =  d['All'].front()	
		while t - w > 1000 and not d['All'].empty():
			w =  d['All'].front()
			d['All'].pop()
		d['All'].push(t)

		if mx['All'] < d['All'].size():		
			mx['All'] = d['All'].size()
			mx_l['All'] = d['All'].front
			

def output():
	for i in d:
		print(i, "Maximum number of trades - ", mx[i], " take place at ", time(mx_l[i] + left))
count()
output()
f.close()		