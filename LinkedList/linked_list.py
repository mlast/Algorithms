from node import *

class LinkedList(object):
	length = 0
	head = None

	def __init__(self):
		pass

	def __len__(self):
		return self.length

	def __contains__(self,key):
		n = self.head
		while n is not None:
			if n.getData() == key:
				return True
			n = n.getNext()
		return False

	def __setitem__(self,key,item):
		if key < self.length and key>=0:
			n = self.head
			for _ in range(0,key):
				n = n.getNext()
			n.setData(item)

	def __getitem__(self,key):
		if key < self.length and key >=0:
			n = self.head
			for _ in range(0,key):
				n = n.getNext()
			return n.getData()

	def __str__(self):
		result = '['
		for i in range(0,self.length):
			result += str(self[i])
			if i < self.length -1:
				result += ', '
		result += ']'
		return result

	def add(self, data):
		if self.head is None:
			self.head = Node(data)
			self.length +=1
		else:
			node = self.head
			while node.getNext() is not None:
				node = node.getNext()
			node.addNode(data)
			self.length += 1




l = LinkedList()
l.add(5)
l.add(6)
l.add(7)


for i in range(0,len(l)):
	print (l[i])

l[1] = 8

for i in range(0,len(l)):
	print(l[i])
print(l)

print (5 in l)
print (4 in l)