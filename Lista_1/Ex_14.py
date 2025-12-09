class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def concat_lists(L, M):
    if L is None:
        return M

    current = L
    while current.next is not None:
        current = current.next

    current.next = M
    return L

if __name__ == "__main__":
    L = Node(1)
    L.next = Node(2)
    L.next.next = Node(3)

    M = Node(4)
    M.next = Node(5)

    result = concat_lists(L, M)

    current = result
    while current:
        print(current.data)
        current = current.next
