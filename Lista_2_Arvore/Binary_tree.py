from Lista_2_Arvore.Tree import Tree

class BinaryTree(Tree):

    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')
    
    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')
    
    def sibling(self, p):
        """Return the Position of p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:                   # p must be the root
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
            
    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)