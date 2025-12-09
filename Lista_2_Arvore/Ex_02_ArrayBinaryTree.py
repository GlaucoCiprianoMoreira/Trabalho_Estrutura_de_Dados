class ArrayBinaryTree:
    """Array-based binary tree class"""

    def __init__(self, capacity: int = 20):
        """
        Initializes the array-based binary tree with a given capacity.
        The tree is represented by a Python list.
        """
        self._tree = [None] * capacity  # Initialize with None values
        self._capacity = capacity

    def insert(self, value, index: int):
        """
        Inserts a value at a specific index in the array.
        Handles cases where the index is out of bounds.
        """
        if index < 0 or index >= self._capacity:
            raise IndexError("Index out of bounds for the tree capacity.")
        self._tree[index] = value

    def get_root(self):
        """Returns the value of the root node."""
        return self._tree[0]

    def get_left_child(self, index: int):
        """Returns the value of the left child of the node at the given index."""
        left_child_index = 2 * index + 1
        if left_child_index < self._capacity:
            return self._tree[left_child_index]
        return None

    def get_right_child(self, index: int):
        """Returns the value of the right child of the node at the given index."""
        right_child_index = 2 * index + 2
        if right_child_index < self._capacity:
            return self._tree[right_child_index]
        return None

    def get_parent(self, index: int):
        """Returns the value of the parent of the node at the given index."""
        if index == 0:  # Root has no parent
            return None
        parent_index = (index - 1) // 2
        return self._tree[parent_index]

    def __str__(self):
        """String representation for debugging."""
        return str(self._tree)

# Example usage:
if __name__ == "__main__":
    tree = ArrayBinaryTree(capacity=7)  # A small tree for demonstration

    tree.insert('A', 0)  # Root
    tree.insert('B', 1)  # Left child of A
    tree.insert('C', 2)  # Right child of A
    tree.insert('D', 3)  # Left child of B
    tree.insert('E', 4)  # Right child of B

    print(f"Tree array: {tree}")
    print(f"Root: {tree.get_root()}")
    print(f"Left child of A (index 0): {tree.get_left_child(0)}")
    print(f"Right child of A (index 0): {tree.get_right_child(0)}")
    print(f"Parent of D (index 3): {tree.get_parent(3)}")
    print(f"Parent of C (index 2): {tree.get_parent(2)}")