import collections.abc

# =================================================================
# CLASSES BASE (NECESSÁRIAS PARA HERANÇA DA TreeMap)
# =================================================================

class MapBase(collections.abc.MutableMapping):
    """Classe base abstrata para implementações de mapas."""
    class _Item:
        __slots__ = '_key', '_value'
        def __init__(self, k, v):
            self._key = k
            self._value = v
        def __lt__(self, other):
            return self._key < other._key
        def __eq__(self, other):
            return self._key == other._key

class LinkedBinaryTree:
    """Mockup simplificado de LinkedBinaryTree para suporte ao TreeMap/AVLTreeMap."""
    class Position:
        __slots__ = '_node'
        def __init__(self, node):
            self._node = node
        def element(self):
            return self._node._element
    
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    def __init__(self):
        self._root = None
        self._size = 0

    def root(self):
        return self.Position(self._root) if self._root is not None else None

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    # Métodos Essenciais para TreeMap
    def _validate(self, p):
        return p

    def left(self, p):
        return self.Position(p._node._left) if p._node._left is not None else None

    def right(self, p):
        return self.Position(p._node._right) if p._node._right is not None else None

    def parent(self, p):
        return self.Position(p._node._parent) if p._node._parent is not None else None
    
    # Métodos de alteração (Mocks simplificados para fluxo de inserção/delete)
    def _make_position(self, node):
        return self.Position(node)
    
    def _add_root(self, element):
        if self._root is not None:
            raise ValueError('Root exists')
        self._root = self._Node(element)
        self._size = 1
        return self._make_position(self._root)

    def _add_left(self, p, element):
        node = p._node
        if node._left is not None:
            raise ValueError('Left child exists')
        node._left = self._Node(element, node)
        self._size += 1
        return self._make_position(node._left)

    def _add_right(self, p, element):
        node = p._node
        if node._right is not None:
            raise ValueError('Right child exists')
        node._right = self._Node(element, node)
        self._size += 1
        return self._make_position(node._right)

    def _replace(self, p, element): # Usado no delete de nó com 2 filhos
        p._node._element = element

    def _delete(self, p): # Deleta um nó com 0 ou 1 filho
        node = p._node
        if node._left and node._right:
            raise ValueError('p has two children, use replacement first')
        
        child = node._left or node._right
        if child is not None:
            child._parent = node._parent
        
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        
        self._size -= 1
        # Clear fields for Position object
        node._parent = node
        return node._element # Return deleted element

    def _attach(self, p, t1, t2):
        raise NotImplementedError("Método _attach não implementado em mock, mas necessário em LinkedBinaryTree real.")

    # Implementação do _restructure (necessário para AVL)
    def _restructure(self, x):
        """Performs trinode restructuring of Position x (avô, pai, nó)."""
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)): # Alinhamento Zig-Zig
            self._rotate(y)
            return y
        else: # Alinhamento Zig-Zag
            self._rotate(x)
            self._rotate(x)
            return x
    
    def _rotate(self, p):
        """Perform a single rotation on p (child) with respect to its parent."""
        x = p._node
        y = x._parent
        z = y._parent # avô
        
        if y is None: return # Não pode rotacionar a raiz

        if x is y._left: # Rotação à direita
            a, b, c = x._left, x, y
            T0, T1, T2, T3 = a and a._right, b._right, c._left and c._right, c and c._right
            y._left = T2
            if T2 is not None: T2._parent = y
            x._right = y
            y._parent = x
            # y._right = T3 # Não é estritamente necessário se não for usada, mas para clareza:
            # if T3 is not None: T3._parent = y

        else: # x is y._right, Rotação à esquerda
            a, b, c = y, x, x._right
            T0, T1, T2, T3 = a and a._left, a and a._right and a._left, b._left, c and c._left
            y._right = T2
            if T2 is not None: T2._parent = y
            x._left = y
            y._parent = x
            # y._left = T1

        # Trata o avô (z)
        if z is None:
            self._root = x # x torna-se a nova raiz
            x._parent = None
        else:
            if y is z._left:
                z._left = x
            else:
                z._right = x
            x._parent = z

        # Atualiza a raiz da subárvore rotacionada
        return x

# =================================================================
# CLASSE MAPA ORDENADO (HERDADA DE LinkedBinaryTree e MapBase)
# =================================================================

class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree."""

    class Position(LinkedBinaryTree.Position):
        """Override Position para acessar key/value do Item."""
        def key(self):
            return self.element()._key
        def value(self):
            return self.element()._value

    _Item = MapBase._Item # Usa a classe _Item definida na MapBase

    def _subtree_search(self, p, k):
        """Retorna a Position com key k, ou o último nó pesquisado (vizinho)."""
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
            else:
                return p
        else: # k > p.key()
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
            else:
                return p

    def _subtree_first_position(self, p):
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def first(self):
        return self._subtree_first_position(self.root()) if not self.is_empty() else None

    # Hooks de rebalanceamento (vazios na BST padrão)
    def _rebalance_insert(self, p): pass
    def _rebalance_delete(self, p): pass
    def _rebalance_access(self, p): pass

    # Métodos Map Padrão
    def __getitem__(self, k):
        if self.is_empty():
            raise KeyError(f'Key Error: {repr(k)}')
        p = self._subtree_search(self.root(), k)
        self._rebalance_access(p) 
        if k != p.key():
            raise KeyError(f'Key Error: {repr(k)}')
        return p.value()

    def __setitem__(self, k, v):
        if self.is_empty():
            leaf = self._add_root(self._Item(k,v))
        else:
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                p.element()._value = v
                self._rebalance_access(p)
                return
            else:
                item = self._Item(k,v)
                if k < p.key():
                    leaf = self._add_left(p, item)
                else:
                    leaf = self._add_right(p, item)
                self._rebalance_insert(leaf)

    def __len__(self): return self._size

    def __iter__(self):
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p) # Assumindo que 'after' está implementado (como na sua versão)
    
    # Implementação de 'after' simplificada para o mock
    def after(self, p):
        if self.right(p) is not None:
            walk = self.right(p)
            while self.left(walk) is not None:
                walk = self.left(walk)
            return walk
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above
    
    # ... Outros métodos de TreeMap (delete, find_ge, etc. omitidos por brevidade)
    # ... Mas você precisaria implementá-los se fossem chamados na AVLTreeMap.

# =================================================================
# CLASSE AVLTreeMap
# =================================================================

class AVLTreeMap(TreeMap):
    """Sorted map implementation using an AVL tree. 
    (Herda de TreeMap, que herda das classes base)"""

    # ---------------------- nested _Node class ----------------------
    class _Node(TreeMap._Node):
        """Node class for AVL maintains height value for balancing."""
        __slots__ = '_height'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0     # will be recomputed during balancing

        def left_height(self):
            """Retorna a altura do filho esquerdo (0 se None)."""
            return self._left._height if self._left is not None else 0

        def right_height(self):
            """Retorna a altura do filho direito (0 se None)."""
            return self._right._height if self._right is not None else 0

    # ---------------------- positional-based utility methods ----------------------
    def _recompute_height(self, p):
        """Recalcula a altura do nó em p com base em seus filhos."""
        p._node._height = 1 + max(p._node.left_height(), p._node.right_height())

    def _isbalanced(self, p):
        """Retorna True se o nó em p está balanceado."""
        return abs(p._node.left_height() - p._node.right_height()) <= 1

    def _tall_child(self, p, favorleft=False): # parameter controls tiebreaker
        """Retorna o filho mais alto de p."""
        if p._node.left_height() + (1 if favorleft else 0) > p._node.right_height():
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self, p):
        """Retorna o neto mais alto de p (para reestruturação)."""
        child = self._tall_child(p)
        # Se o filho é esquerdo, favorece o neto esquerdo; se o filho é direito, favorece o neto direito.
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)

    def _rebalance(self, p):
        """Percorre a árvore do nó p até a raiz, rebalanceando nós desbalanceados."""
        while p is not None:
            old_height = p._node._height
            
            # Recalcula a altura de p primeiro
            self._recompute_height(p) 

            if not self._isbalanced(p):
                # Desbalanceado: performa a reestruturação trinodal (g-p-x)
                # p se torna a raiz da subárvore reestruturada
                p = self._restructure(self._tall_grandchild(p)) # p é agora o centro (b)
                
                # Recalcula alturas dos 3 nós envolvidos após a rotação
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
                self._recompute_height(p) # Altura final da nova raiz da subárvore

            if p._node._height == old_height:
                # Se a altura não mudou, o rebalanceamento acabou
                p = None 
            else:
                # Continua subindo
                p = self.parent(p) 
    
    def __delitem__(self, k):
        """Remove item associado com a chave k (levanta KeyError se não encontrado)."""
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p) # Depende da implementação correta de delete(p)
                return 
            self._rebalance_access(p) 
        raise KeyError('Key Error: ' + repr(k))

    # ---------------------- override balancing hooks ----------------------
    def _rebalance_insert(self, p):
        """Sobrescreve o hook após a inserção para iniciar o rebalanceamento."""
        self._rebalance(p)

    def _rebalance_delete(self, p):
        """Sobrescreve o hook após a exclusão para iniciar o rebalanceamento."""
        self._rebalance(p)


# =================================================================
# TESTE
# =================================================================

if __name__ == "__main__":
    
    # --------------------- Métodos de Teste Auxiliares (Opcional) ---------------------
    # Para o teste funcionar, adicionamos métodos utilitários à AVLTreeMap
    def get_root_height(self):
        root = self.root()
        return root._node._height if root else 0
    AVLTreeMap.get_root_height = get_root_height

    def is_tree_balanced(self):
        def check_balance(p):
            if p is None: return True, 0 # É balanceado, altura 0
            
            left_balanced, left_height = check_balance(self.left(p))
            right_balanced, right_height = check_balance(self.right(p))
            
            is_local_balanced = abs(left_height - right_height) <= 1 and left_balanced and right_balanced
            current_height = 1 + max(left_height, right_height)
            
            # Verifica se a altura armazenada é a correta (para debugging)
            if p._node._height != current_height:
                 print(f"Alerta: Altura incorreta no nó {p.key()}. Esperado: {current_height}, Armazenado: {p._node._height}")
            
            return is_local_balanced, current_height

        root = self.root()
        if root is None: return True
        balanced, _ = check_balance(root)
        return balanced
        
    AVLTreeMap.is_tree_balanced = is_tree_balanced
    # ----------------------------------------------------------------------------------

    print("--- Teste de AVLTreeMap ---")

    # 1. Criação e Inserção
    avl_map = AVLTreeMap()
    print("Criando um mapa AVL...")

    # Exemplo de inserção que força rotações (1-2-3 ou 3-2-1)
    elementos = [
        (10, 'A'), 
        (5, 'B'),  # Causa desbalanceamento 
        (15, 'C'), 
        (3, 'D'),  # Causa rotação (e.g., 5-10 desbalanceado)
        (7, 'E'), 
        (12, 'F'), 
        (18, 'G'), 
        (1, 'H')   # Causa mais rotações
    ]
    
    print("\n[Image of AVL Tree Rotations]")

    for key, value in elementos:
        avl_map[key] = value # Usa __setitem__ que chama _rebalance_insert
        print(f"Inserido: ({key}, '{value}'). Altura da raiz: {avl_map.get_root_height()}")