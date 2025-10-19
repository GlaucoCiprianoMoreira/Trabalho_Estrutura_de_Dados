class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Fila circular cheia")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Fila circular vazia")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Fila circular vazia")
        return self.queue[self.front]

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return "CircularQueue([])"
        items = []
        index = self.front
        for _ in range(self.size):
            items.append(str(self.queue[index]))
            index = (index + 1) % self.capacity
        return "CircularQueue([" + ", ".join(items) + "])"
    

if __name__ == "__main__":
    cq = CircularQueue(5)
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    print(cq)  # CircularQueue([10, 20, 30])
    print("Dequeued:", cq.dequeue())  # Dequeued: 10
    print(cq)  # CircularQueue([20, 30])
    cq.enqueue(40)
    cq.enqueue(50)
    cq.enqueue(60)
    print(cq)  # CircularQueue([20, 30, 40, 50, 60])
    print("Front element:", cq.peek())  # Front element: 20
    print("Queue size:", len(cq))  # Queue size: 5