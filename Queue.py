import queue
q = queue.Queue()


q.put('Hallo')
q.put('Welt')
q.put('Mars')

print(q.get())
print(q.get())

while not q.empty():
    element = q.get()
    print(element)