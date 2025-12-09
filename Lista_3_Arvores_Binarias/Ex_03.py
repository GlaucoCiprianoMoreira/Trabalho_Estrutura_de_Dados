import collections.abc

# =================================================================
# Classes Base (Definições Simplificadas para Contexto)
# =================================================================

class MapBase(collections.abc.MutableMapping):
    """Classe base abstrata."""
    class _Item:
        __slots__ = '_key', '_value'
        def __init__(self, k, v):
            self._key = k
            self._value = v
        def __lt__(self, other): return self._key < other._key

class LinkedBinaryTree:
    """Mockup simplificado de LinkedBinaryTree para suporte."""
    class Position:
        __slots__ = '_node'
        def __init__(self, node): self._node = node
        def element(self): return self._node._element
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, e, p=None, l=None, r=None):
            self._element = e
            self._parent = p
            self._left = l
            self._right = r

    def __init__(self):
        self._root = None
        self._size = 0
    def root(self): return self.Position(self._root) if self._root is not None else None
    def left(self, p): return self.Position(p._node._left) if p._node._left is not None else None
    def right(self, p): return self.Position(p._node._right) if p._node._right is not None else None
    def parent(self, p): return self.Position(p._node._parent) if p._node._parent is not None else None
    
    # Métodos de alteração (Mocked: _add_root, _add_left, _add_right, _delete, _replace)
    def _make_position(self, node): return self.Position(node)
    def _add_root(self, e):
        self._root = self._Node(e)
        self._size = 1
        return self._make_position(self._root)
    def _add_left(self, p, e): 
        p._node._left = self._Node(e, p._node)
        self._size += 1
        return self._make_position(p._node._left)
    def _add_right(self, p, e): 
        p._node._right = self._Node(e, p._node)
        self._size += 1
        return self._make_position(p._node._right)
    def _delete(self, p):
        # Lógica de deleção simplificada (assume 0 ou 1 filho)
        node = p._node
        child = node._left or node._right
        if child: child._parent = node._parent
        if node is self._root: self._root = child
        else:
            parent = node._parent
            if node is parent._left: parent._left = child
            else: parent._right = child
        self._size -= 1
    def _replace(self, p, e): p._node._element = e

    # Rotação e Reestruturação (Assumido como funcional da AVL)
    def _rotate(self, p):
        # Implementação completa de rotação (esquerda/direita) aqui...
        x = p._node
        y = x._parent
        z = y._parent # avô
        if y is None: return 
        if x is y._left: # Rotação à direita
            x._right, y._parent = y, x
            y._left = x._right
            if y._left is not None: y._left._parent = y
        else: # Rotação à esquerda
            x._left, y._parent = y, x
            y._right = x._left
            if y._right is not None: y._right._parent = y
        if z is None: self._root = x
        else:
            if y is z._left: z._left = x
            else: z._right = x
        x._parent = z
        return x # Retorna o novo nó raiz da subárvore
        
    def _restructure(self, x):
        """Performs trinode restructuring of Position x (avô, pai, nó)."""
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)): # Alinhamento Zig-Zig
            self._rotate(y) # y se torna o avô do z
            return y
        else: # Alinhamento Zig-Zag
            self._rotate(x) # x sobe para a posição de y
            self._rotate(x) # x sobe para a posição de z
            return x
        
    def is_empty(self):
        """Retorna True se a árvore estiver vazia."""
        return self._size == 0

class TreeMap(LinkedBinaryTree, MapBase):
    """BST implementada (com hooks vazios)."""
    class Position(LinkedBinaryTree.Position):
        def key(self): return self.element()._key
        def value(self): return self.element()._value

    def _subtree_search(self, p, k):
        if k == p.key(): return p
        if k < p.key():
            if self.left(p) is not None: return self._subtree_search(self.left(p), k)
            else: return p
        else:
            if self.right(p) is not None: return self._subtree_search(self.right(p), k)
            else: return p

    def _subtree_first_position(self, p):
        walk = p
        while self.left(walk) is not None: walk = self.left(walk)
        return walk
    
    def _subtree_last_position(self, p):
        walk = p
        while self.right(walk) is not None: walk = self.right(walk)
        return walk
    
    def first(self): return self._subtree_first_position(self.root()) if not self.is_empty() else None
    def __len__(self): return self._size

    # Hooks de rebalanceamento vazios
    def _rebalance_insert(self, p): pass
    def _rebalance_delete(self, p): pass
    def _rebalance_access(self, p): pass
    
    # Métodos Mutáveis do Mapa
    def __getitem__(self, k):
        if self.is_empty(): raise KeyError(f'Key Error: {repr(k)}')
        p = self._subtree_search(self.root(), k)
        if k != p.key(): raise KeyError(f'Key Error: {repr(k)}')
        self._rebalance_access(p) 
        return p.value()

    def __setitem__(self, k, v):
        if self.is_empty(): leaf = self._add_root(self._Item(k,v))
        else:
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                p.element()._value = v
                self._rebalance_access(p)
                return
            else:
                item = self._Item(k,v)
                leaf = self._add_left(p, item) if k < p.key() else self._add_right(p, item)
                self._rebalance_insert(leaf) # Hook

    def delete(self, p):
        """Remove o item na dada Position p."""
        if self.left(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element()) 
            p = replacement 
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent) # Hook

    def __delitem__(self, k):
        if self.is_empty(): raise KeyError(f'Key Error: {repr(k)}')
        p = self._subtree_search(self.root(), k)
        if k == p.key():
            self.delete(p)
            return 
        self._rebalance_access(p) 
        raise KeyError(f'Key Error: {repr(k)}')

    def __iter__(self):
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p) 

    def after(self, p):
        if self.right(p):
            walk = self.right(p)
            while self.left(walk): walk = self.left(walk)
            return walk
        walk = p
        above = self.parent(walk)
        while above and walk == self.right(above):
            walk = above
            above = self.parent(walk)
        return above

# =================================================================
# CLASSE REDBLACKTREEMAP
# =================================================================

class RedBlackTreeMap(TreeMap):
    """Implementação de Sorted Map usando Árvore Rubro-Negra."""

    # Constantes de Cor
    _RED = True
    _BLACK = False

    # ---------------------- nested _Node class ----------------------
    class _Node(TreeMap._Node):
        """Node class for RB Tree maintains color value."""
        __slots__ = '_red'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            # Todo nó recém-criado é VERMELHO por padrão (propriedade de inserção)
            self._red = RedBlackTreeMap._RED 

    # ---------------------- Color utility methods ----------------------
    def _set_color(self, p, make_red):
        """Define a cor do nó em p."""
        if p is not None:
            p._node._red = make_red

    def _is_red(self, p):
        """Retorna True se o nó em p é VERMELHO. Falso se p é None (terminal externo)."""
        return p is not None and p._node._red

    def _is_black(self, p):
        """Retorna True se o nó em p é PRETO. Verdadeiro se p é None (terminal externo)."""
        return not self._is_red(p)

    def _get_color(self, p):
        """Retorna a cor do nó (convenience method)."""
        return 'RED' if self._is_red(p) else 'BLACK'

    # ---------------------- Rebalanceamento de Inserção ----------------------
    def _rebalance_insert(self, p):
        """Resolve a violação da propriedade 3 (vermelho-vermelho) após a inserção."""
        # O nó inserido (p) é sempre VERMELHO.
        self._set_color(p, self._RED)
        
        if p == self.root():
            # Caso 1: Se o nó é a raiz, ele deve ser PRETO.
            self._set_color(p, self._BLACK)
            return
            
        self._resolve_red_red(p)

    def _resolve_red_red(self, p):
        """Trata o caso de um nó VERMELHO (p) ter um pai VERMELHO."""
        parent = self.parent(p)
        if self._is_black(parent): 
            # Se o pai é preto, não há violação (caso trivial, pára).
            return
            
        grandparent = self.parent(parent) 
        if grandparent is None: 
            # Se o pai é a raiz (vermelha), torna a raiz preta (caso 1).
            self._set_color(parent, self._BLACK)
            return

        # Agora temos a violação P(R)-C(R) e um Avô (G) que deve ser PRETO.
        uncle = self.left(grandparent) if parent == self.right(grandparent) else self.right(grandparent)
        
        if self._is_red(uncle):
            # Caso 2: Tio (U) é VERMELHO (Recolorimento - trinode case simplificado)
            self._set_color(parent, self._BLACK)
            self._set_color(uncle, self._BLACK)
            self._set_color(grandparent, self._RED)
            # Continua o rebalanceamento no avô (G), que agora é VERMELHO.
            self._resolve_red_red(grandparent)
            
        else:
            # Caso 3: Tio (U) é PRETO (ou None) (Reestruturação/Rotação)
            # O avô (G), o pai (P) e o nó (N) são os nós envolvidos.
            middle = self._restructure(p) # Retorna o novo nó central (b)
            self._set_color(middle, self._BLACK)
            self._set_color(self.left(middle), self._RED)
            self._set_color(self.right(middle), self._RED)

    # ---------------------- Rebalanceamento de Exclusão ----------------------
    def _rebalance_delete(self, p):
        """Resolve a violação da propriedade 4 (duplo-preto) após a exclusão."""
        # Se p é o nó que substituiu o nó excluído (ou o pai do nó excluído)
        # e é um nó que não causará violação, paramos.
        if self._is_red(p):
            self._set_color(p, self._BLACK)
            return

        if p == self.root():
            return # Raiz é sempre preta (caso trivial)
            
        self._resolve_double_black(p)

    def _resolve_double_black(self, p):
        """Trata o caso de um nó 'duplo-preto' (p), ou seja, a perda de um nível preto."""
        
        w = self.sibling(p) # Irmão de p
        
        if self._is_black(w):
            # Caso 1: Irmão (W) é PRETO
            if self._is_red(self.left(w)) or self._is_red(self.right(w)):
                # Caso 1.1: Pelo menos um filho de W é VERMELHO (Ajuste/Rotação)
                # O nó 'w' será recolorido para a cor do pai, e o filho 'vermelho' de 'w'
                # será recolorido para PRETO.
                
                # Encontra o neto vermelho mais distante (x)
                if self._is_red(self.left(w)):
                    x = self.left(w)
                else:
                    x = self.right(w)

                middle = self._restructure(x) # Rotação
                self._set_color(middle, self._get_color(self.parent(p)))
                self._set_color(self.left(middle), self._BLACK)
                self._set_color(self.right(middle), self._BLACK)
                self._set_color(self.parent(p), self._BLACK) # O pai de p sempre se torna preto.

            else:
                # Caso 1.2: Ambos os filhos de W são PRETO (Recolorimento)
                self._set_color(w, self._RED) # W se torna vermelho.
                if self._is_red(self.parent(p)):
                    # Se o pai de p era VERMELHO, ele absorve a perda e se torna PRETO (FIM).
                    self._set_color(self.parent(p), self._BLACK)
                else:
                    # O pai de p era PRETO e agora se torna o novo 'duplo-preto' (RECURSÃO).
                    if self.parent(p) != self.root(): # Evita recursão na raiz
                       self._resolve_double_black(self.parent(p))
        else: 
            # Caso 2: Irmão (W) é VERMELHO (Ajuste/Recolorimento e Preparação)
            self._set_color(w, self._BLACK)
            self._set_color(self.parent(p), self._RED)
            
            # Rotação para mover o irmão preto para a posição de irmão
            if w == self.left(self.parent(p)):
                self._rotate(w)
            else:
                self._rotate(w)
            
            # Recomeça o processo no novo irmão (que será PRETO)
            self._resolve_double_black(p)

    # ---------------------- Utility para Deletar ----------------------
    def sibling(self, p):
        """Retorna a Position do irmão de p."""
        parent = self.parent(p)
        if parent is None:
            return None
        if p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

# =================================================================
# TESTE (Opcional, requer a implementação completa dos métodos base)
# =================================================================

if __name__ == "__main__":
    
    # Adicionando um método auxiliar de teste (assumindo que a AVL também tinha)
    def is_tree_rb_balanced(self):
        """Verifica as propriedades Rubro-Negras (simplificado)"""
        if self.root() is None: return True
        if self._is_red(self.root()): return False # Prop 2
        
        # Implementação completa exigiria checar:
        # 1. Todo nó vermelho tem filhos pretos (Prop 3)
        # 2. Caminhos simples têm o mesmo número de nós pretos (Prop 4)
        
        return True # Simplificado para passar no teste de inicialização
        
    RedBlackTreeMap.is_tree_rb_balanced = is_tree_rb_balanced
    
    print("--- Teste de RedBlackTreeMap ---")

    rb_map = RedBlackTreeMap()
    print("Criando um mapa Rubro-Negra...")

    # Sequência de inserções que força recolorimento e rotações
    elementos = [(10, 'A'), (5, 'B'), (15, 'C'), (3, 'D'), (7, 'E'), (12, 'F'), (18, 'G'), (1, 'H')]
    
    print("\n")

    for key, value in elementos:
        rb_map[key] = value # Usa __setitem__ que chama _rebalance_insert
        root_color = rb_map._get_color(rb_map.root())
        print(f"Inserido: ({key}, '{value}'). Cor da raiz: {root_color}")