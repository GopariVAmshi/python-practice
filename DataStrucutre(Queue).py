import queue

l = queue.Queue(maxsize = 6)


l.put(3)
l.put(1)
l.put(2)
l.put(4)
l.put(5)
l.put(3)
l.put(4)

print(list(l.queue))
print("Queue FUll:",l.full())
print(l.get())
print(list(l.queue))
print("Queue Full:",l.full())