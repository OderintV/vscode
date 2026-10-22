class CircularQueue:
    def __init__(self, size):
        self.queue = [None]*size
        self.max_size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.max_size == self.front:
            return "Queue is Full"
        elif self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            return "Queue is Empty"
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return item
