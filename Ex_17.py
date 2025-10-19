class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse_recursive(self):
        self.head = self._reverse_recursive_util(self.head)

    def _reverse_recursive_util(self, current):
        if current is None or current.next is None:
            return current
        
        new_head = self._reverse_recursive_util(current.next)
        
        current.next.next = current
        current.next = None
        
        return new_head
    

lista = LinkedList()
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)

print(lista)

lista.reverse_recursive()

print(lista)