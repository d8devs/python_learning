import queue

q = queue.PriorityQueue()
q.put((10, "Hallo Welt"))
q.put((20, "Hallo Mars"))
q.put((15, "Hallo Jupiter"))


print(q.get())
print(q.get())


# A Example without PriorityQueue
text = "A A A B C D E E E F F G G H H E E E"
d = {}
for word in text.split(" "):
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1

print(d)
# A Example with PriorityQueue
text = "A A A B C D E E E F F G G H H E E E"
d = {}

for word in text.split(" "):
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1

pq = queue.PriorityQueue()

for word, number in d.items():
    pq.put((-number, word))

print(pq.get())
print(pq.get())