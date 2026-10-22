class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

q = Queue()
q.enqueue('A')
q.enqueue('B')  
q.enqueue(2)
q.enqueue(3.14)
q.dequeue() 
q.dequeue()
q.dequeue()
