class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
        if len(self.items) > 10:
            print("Queue is full")
            self.items.pop(0)
    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None
    def is_empty(self):
        return len(self.items) == 0
    def __str__(self):
        return f"Queue{self.items}"
    

q = Queue()
q.enqueue(7)
q.enqueue(32)
print(q)
q.dequeue()
print(q)

