class Node(object):
	data = None
	next = None

	def __init__(self, data):
		self.data = data

	def addNode(self,data):
		self.next = Node(data)

	def getNext(self):
		return self.next

	def getData(self):
		return self.data

	def setData(self,data):
		self.data = data
