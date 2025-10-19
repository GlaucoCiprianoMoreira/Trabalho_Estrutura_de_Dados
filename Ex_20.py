class Node:
    def __init__(self, element, prev, next):
        self.element = element
        self.prev = prev
        self.next = next

class DoublyLinkedBase:
    def __init__(self):
        self.header = Node(None, None, None)
        self.trailer = Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = Node(e, predecessor, successor)
        predecessor.next = newest
        successor.prev = newest
        self.size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        element = node.element
        node.prev = node.next = node.element = None
        return element

    def add_last(self, e):
        return self._insert_between(e, self.trailer.prev, self.trailer)

    def print_list(self):
        current = self.header.next
        while current is not self.trailer:
            print(current.element, end=" ")
            current = current.next
        print()

    def reverse(self):
        current = self.header
        while current is not None:
            current.prev, current.next = current.next, current.prev
            current = current.prev

        self.header, self.trailer = self.trailer, self.header


if __name__ == '__main__':
    list = DoublyLinkedBase()
    print(f"Lista criada. Vazia? {list.is_empty()}")

    list.add_last('A')
    list.add_last('B')
    list.add_last('C')
    list.add_last('D')

    print(f"\nTamanho da lista: {len(list)}")

    print("Estado Original:")
    list.print_list()

    list.reverse()
    print("\n--- Invertendo a Lista ---")

    print("Estado Invertido:")
    list.print_list()