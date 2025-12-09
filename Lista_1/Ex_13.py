class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def encontrar_penultimo(head):
    if head is None or head.next is None:
        return None

    current = head
    while current.next.next is not None:
        current = current.next

    return current

if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    penultimo = encontrar_penultimo(head)
    if penultimo:
        print("Penúltimo nó:", penultimo.data)
    else:
        print("A lista não possui penúltimo nó.")
