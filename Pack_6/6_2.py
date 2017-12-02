class _Node:
    def __init__(self, _element, _sitename, _prev,_next):
        self._element =_element
        self._sitename = _sitename
        self._prev =_prev
        self._next =_next
		
class DoublyLinkedBase:
    def __init__ (self):
        self._header = _Node(0, None, None, None)
        self._trailer = _Node(100000, None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, url, predecessor, successor):

        newest = _Node(e, url, predecessor, successor) 
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        node._prev = node._next = node._element = None
       
    def _find(self, name):
        x = self._header
        while(x != self._trailer):
            if x._sitename == name:
                return x
            x = x._next
        return False
          
class DoublyLinkedList(DoublyLinkedBase):
    def from_site(self, url):
        s = self._find(url)
        if s == False:
            return self._insert_between(1, url, self._header, self._header._next)       
        x = s
        count = s._element
        while(x != self._trailer):
            if count + 1 <= x._next._element:
                self._insert_between(count + 1, url, x, x._next)
                return self._delete_node(s)
            x = x._next
        return self._insert_between(count + 1, url, self._trailer._prev, self._trailer)
    
    def from_client(self, count):
        if not self.is_empty():
            x = self._trailer._prev  
            i = 1
            print("Top", count, "sites: ")
            while x != self._header and i <= count:
                print(str(i) + ')', x._sitename)
                i += 1
                x = x._prev
            print()
			
def menu():
	b = DoublyLinkedList()
	base = DoublyLinkedList()
	b.from_site("vk.com")
	b.from_site("google.com")
	b.from_site("google.com")
	b.from_site("yandex.ru")
	b.from_site("wiki.ru")
	b.from_client(3)
	b.from_site("vk.com")
	b.from_site("vk.com")
	b.from_client(4)
	while (input("exit?(y/n)") != 'y'):
		com = input("s - site , c - client ")
		if com == 's':
			url = input("Input url: ")
			base.from_site(url)
		elif com == 'c':
			url = int(input("Input count of sites: "))
			base.from_client(url)
		else:
			print("Unknown operation.")

menu()
