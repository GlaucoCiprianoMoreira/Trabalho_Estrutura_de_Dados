class Tree:
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')
        
        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')
        
        def __ne__(self, other):
            return not (self == other)
        
    def root(self):
        raise NotImplementedError('must be implemented by subclass')
    
    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')
    
    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')
    
    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')
    
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p
    
    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0
    
    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0