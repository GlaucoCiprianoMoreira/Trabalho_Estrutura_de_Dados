class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def remove_duplicates(self):
        if not self.head:
            return

        seen = set()
        current = self.head
        while current:
            if current.data in seen:
                next_node = current.next
                prev_node = current.prev

                if prev_node:
                    prev_node.next = next_node
                else:
                    self.head = next_node

                if next_node:
                    next_node.prev = prev_node

                temp = current
                current = next_node
                del temp
            else:
                seen.add(current.data)
                current = current.next

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(2)
    dll.append(4)
    dll.append(1)
    dll.append(5)

    dll.display()

    dll.remove_duplicates()

    dll.display()