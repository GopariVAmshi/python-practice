class Queue:
	def __init__(self,max_size):
		self.max_size = max_size
		self.elements = [None] * self.max_size
		self.rear = -1
		self.front = 0

	def is_full(self):
		if self.rear == self.max_size-1:
			return True
		return False

	def is_empty(self):
		if self.front > self.rear:
			return True
		return False

	def enqueue(self,data):
		if self.is_full():
			print("Queue is full")
		else:
			self.rear +=1
			self.elements[self.rear] = data
	def dequeue(self):
		if self.is_empty():
			print("Queue is empty")
		else:
			data = self.elements[self.front]
			self.front +=1
			return data
	def get_max_size(self):
		print("\nmaximum size of queue is:",self.max_size,"\n")
	def display(self):
		print("------------------")
		for index in range(self.front,self.rear+1):
			print(self.elements[index],"\n")
		print("------------------")
	def split(self,q):
		even = []
		odd = []
		for i in iter(q.get(),None):
			if i%2 == 0:
				even.append(i)
			else:
				odd.append(i)
		print("even list is:", even)
		print("Odd list is:",odd)



q = Queue(4)
q.get_max_size()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)


q.display()

q.dequeue()

q.display()
q.split(q)