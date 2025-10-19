class ArrayQueue:
    def __init__(self):
        self._data = []
        self._front = 0

    def is_empty(self):
        return len(self._data) == 0

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self._data[self._front]
        self._front += 1
        if self._front > len(self._data) // 2:
            self._data = self._data[self._front:]
            self._front = 0
        return item

    def first(self):
        if self.is_empty():
            raise IndexError("First from empty queue")
        return self._data[self._front]

    def size(self):
        return len(self._data) - self._front