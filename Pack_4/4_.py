def get_time(line):
    return int(line[0:2]) * 60 * 60 * 1000 + int(line[3:5]) * 60 * 1000 + int(line[6:8]) * 1000 + int(line[9:12])


def time(t):
	h = t // 3600000 
	m = t // 60000 - h * 60
	s = t // 1000 - h * 3600 - m * 60 
	ms = t - h *3600000 - m * 60000 - s * 1000
	return str(h) + ":" + str(m) + ":" + str(s) + ":" + str(ms)
	
pin = open("TRD2.csv","r")
a = pin.readline()

def For_wolf_of_Wall_Street():
	
	d = {'V':None,'D':None,'X':None,'Y':None,'B':None,'J':None,'Q':None,'Z':None,'K':None,'P':None, 'All':None}
	max       = {'V':0,'D':0,'X':0,'Y':0,'B':0,'J':0,'Q':0,'Z':0,'K':0,'P':0,'All':0}
	max_time = {'V':0,'D':0,'X':0,'Y':0,'B':0,'J':0,'Q':0,'Z':0,'K':0,'P':0,'All':0}
	for i in d:
		d[i] = list()
	
	str = pin.readline()
	str = str.split(',')
	
	Global_Start_Time = get_time(str[0])
	
	while (str[0] != ''):
		## для каждой бирже в отдельности 
		Exchange = str[3][0]
		Right_Time = get_time(str[0]) - Global_Start_Time
		if (len(d[Exchange]) > 0): Left_Time = d[Exchange][0]
		else:                     Left_Time = 0
		
		while Right_Time - Left_Time > 1000 and len(d[Exchange]) > 0: Left_Time = d[Exchange].pop(0)
		
		d[Exchange].append(Right_Time)
		
		if (max[Exchange] < len(d[Exchange])):
			max[Exchange] = len(d[Exchange])
			max_time[Exchange] = d[Exchange][0]
		## for all stock exchange
		Exchange = 'All'
		if (len(d[Exchange]) > 0): Left_Time = d[Exchange][0]
		else:                     Left_Time = 0
		
		while Right_Time - Left_Time > 1000 and len(d[Exchange]) > 0: Left_Time = d[Exchange].pop(0)
		
		d[Exchange].append(Right_Time)
		
		if (max[Exchange] < len(d[Exchange])):
			max[Exchange] = len(d[Exchange])
			max_time[Exchange] = d[Exchange][0]
		
		##read new line 
		str = pin.readline()
		str = str.split(',')
	print('')
	print('')
	print("Steaks, stocks - what's the difference?")
	print('')
	for i in d:
		print('%-3s' % i, '%-12s' % time(max_time[i] + Global_Start_Time), max[i])
		
	return 0	

For_wolf_of_Wall_Street()