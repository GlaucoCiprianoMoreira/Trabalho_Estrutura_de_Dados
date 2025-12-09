class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_front(self, item):
        new_node = DoubleNode(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1

    def add_rear(self, item):
        new_node = DoubleNode(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def remove_front(self):
        if self.is_empty():
            raise Exception("Deque vazio")
        item = self.front.data
        self.front = self.front.next
        if self.front is not None:
            self.front.prev = None
        else:
            self.rear = None
        self.size -= 1
        return item

    def remove_rear(self):
        if self.is_empty():
            raise Exception("Deque vazio")
        item = self.rear.data
        self.rear = self.rear.prev
        if self.rear is not None:
            self.rear.next = None
        else:
            self.front = None
        self.size -= 1
        return item

    def peek_front(self):
        if self.is_empty():
            raise Exception("Deque vazio")
        return self.front.data

    def peek_rear(self):
        if self.is_empty():
            raise Exception("Deque vazio")
        return self.rear.data

    def __len__(self):
        return self.size

    def __str__(self):
        items = []
        current = self.front
        while current is not None:
            items.append(str(current.data))
            current = current.next
        return "LinkedDeque([" + ", ".join(items) + "])"
    

if __name__ == "__main__":
    ld = LinkedDeque()
    ld.add_rear(10)
    ld.add_rear(20)
    ld.add_front(5)
    print(ld)  # LinkedDeque([5, 10, 20])
    print("Remover da frente:", ld.remove_front())
    print("Remover do final:", ld.remove_rear())
    print(ld)  # LinkedDeque([10])