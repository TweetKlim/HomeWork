import random 

def print_r():
	global river
	global length
	for i in range(length):
		if(river[i] == 0):
			print("~", end="")
		else: print(river[i].char , end = "")	
	print()
	
class Fish():
	def __init__(self):
		self.char = 'F'
		
class Bear():
	def __init__(self):
		self.char = 'B'
		self.hungry = 0
	
def step():
	global length
	global river
	global free_Position
	stop = 0
	for i in range(length):
		if(river[i] != 0 and not stop):
			if(river[i].char == 'B'):
				river[i].hungry += 1
				## technology smart hungry bear
				if(length - 1 != i): 
					if(river[i + 1] != 0):
						if(river[i + 1].char == 'F'):
							river[i + 1] = river[i]
							river[i] = 0
							stop += 1
							river[i+1].hungry = 0
							continue
				if(i != 0):
					if(river[i - 1] != 0):
						if(river[i - 1].char == 'F'):
							river[i - 1] = river[i]
							river[i] = 0
							river[i-1].hungry = 0
							continue
				## end of technology
				move = random.randint(0, 1)
				if(i == 0 and move == 0): move = 1
				if(i == length - 1 and move == 1): move = 0
				if(river[i + move * 2 - 1] == 0):
					river[i + move * 2 - 1] = river[i]
					river[i] = 0
					stop += move
				else:
					while(free_Position):
						poz = random.randint(0, length - 1)
						if (river[poz] == 0):
							if(random.randint(0, 2)):
								river[poz] = Bear()
								stop += move
								free_Position -= 1
							break
							
			elif(river[i].char == 'F'):
				move = random.randint(0, 1)
				if(i == 0 and move == 0 or move == 0 and river[i - 1] == 'B'):
					move = 1
				elif(i == length - 1 and move == 1 or move == 1 and river[i + 1] == 'B'):
					move = 0
				##if(move == 0 and river[i - 1] == 'B'): continue
				##if(move == 1 and river[i + 1] == 'B'): continue
				if(river[i + move * 2 - 1] == 0):
					river[i + move * 2 - 1] = river[i]
					river[i] = 0
					stop += move
				elif(river[i + move * 2 - 1] == 'F'):
					while(free_Position):
						poz = random.randint(0, length - 1)
						if (river[poz] == 0):	
							if(random.randint(0, 2)):
								river[poz] = Fish()
								stop += move
								free_Position -= 1
							break
		elif(stop):
			stop = 0
			continue
		
def simulation():
	global length
	global number_Bear
	global number_Fish
	global iteration
	global river
	global free_Position
	free_Position = length - number_Fish
	for i in range(length):
		if (number_Fish > 0):
			if (random.randint(0, length - i - number_Fish) < number_Fish):
				river[i] = Fish()
				number_Fish -= 1
	for i in range(length):
		if (river[i] == 0 and number_Bear > 0 and free_Position > 0):
			if (random.randint(0, (free_Position - number_Bear)) <= number_Bear):
				river[i] = Bear()
				number_Bear -= 1
			free_Position -= 1
	
	print_r()	
	print()
	for i in range(iteration):
		## chech how many moves bears did not eat
		free_Position = 0
		for i in range(length):
			if(river[i] != 0):
				if(river[i].char == 'B'): 
					if(river[i].hungry == number_Step_W_Food):
						river[i] = 0
			else: free_Position += 1
		step()
		print_r()
		print()
	
	
free_Position = 0
random.seed()
length = int(input("length river  "))
number_Fish = int(input("Number of fish  "))
number_Bear = int(input("Number of bear  "))
number_Step_W_Food = int(input("Number step without food  "))
iteration = int(input("Iteration  "))
river = [0 for i in range(length + 1)]
print_r()
simulation()
