class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("A fila está vazia")
        dequeued_node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.size -= 1
        return dequeued_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("A fila está vazia")
        return self.front.data

    def get_size(self):
        return self.size
    

if __name__ == "__main__":
    queue = LinkedQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Front element:", queue.peek())  # Output: Front element: 1
    print("Queue size:", queue.get_size())  # Output: Queue size: 3
    print("Dequeued element:", queue.dequeue())  # Output: Dequeued element: 1
    print("Queue size after dequeue:", queue.get_size())  # Output: Queue size after dequeue: 2