
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self.top.data

    def get_size(self):
        return self.size
    
if __name__ == "__main__":
    stack = LinkedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Elemento de cima:", stack.peek())
    print("Tamanho da Pilha:", stack.get_size())
    print("Elemento retirado:", stack.pop())
    print("Tamanho depois da remoção:", stack.get_size())
