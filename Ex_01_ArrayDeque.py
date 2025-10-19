class ArrayDeque:
    def __init__(self):
        self.items = []
    
    def add_first(self, item):
        self.items.insert(0, item)
    
    def add_last(self, item):
        self.items.append(item)
    
    def remove_first(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("remove_front from empty deque")
    
    def remove_last(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("remove_rear from empty deque")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def peek_first(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("peek_front from empty deque")
    
    def peek_last(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek_rear from empty deque")
    
    def __str__(self):
        return "ArrayDeque(" + ", ".join(repr(item) for item in self.items) + ")"