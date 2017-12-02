import lists

class DoublyLinkedCircularList(lists.DoublyLinkedBase):
    def __init__ (self):
        self._header = lists._Node(None, None, None)
        self._header._next = self._header
        self._header._prev = self._header
        self._size = 0
    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._header._prev, self._header)
        
    def delete_first(self):
        if self.is_empty( ):
            raise lists.Empty("List is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty( ):
            raise lists.Empty("List is empty")
        return self._delete_node(self._header._prev)    
    def __str__(self):
        s = '['
        if self._size != 0:
            x = self._header._next         
            s += str(x._element)
            while x._next._element != None:
                x = x._next
                s += ', ' + str(x._element)
        return s + ']'
		
c = DoublyLinkedCircularList()

while input('Сircle?(y/n)') == 'y':
	wDo = input("What to do?(insert/del): ")
	while (wDo != 'insert' and wDo != 'del'):
		print('wrong input')
		wDo = input("What to do?(insert/del): ")	
	pos = input("Input pos(first/last): ")
	while (pos != 'first' and pos != 'last'):
		print('wrong input')
		pos = inputinput("Input pos(first/last): ")	
	if (wDo == 'insert'):
		num = input("num: ")
		if(pos == 'first'):
			c.insert_first(num)
		else:
			c.insert_last(num)
	else:
		if(pos == 'first'):
			c.delete_first()
		else:
			c.delete_last()
			
x = c._header._next 
cycle = int(input("Cycle times: "))
count = 0        
while count < cycle:
	if x._element != None:
		print(x._element)
	else:
		count += 1
	x = x._next
	    
print("List: ", c)
