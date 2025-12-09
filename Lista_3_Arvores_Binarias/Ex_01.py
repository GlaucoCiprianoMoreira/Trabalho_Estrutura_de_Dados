import collections.abc

# ---------------------- Supondo que LinkedBinaryTree seja uma classe base ----------------------
# Para que o código funcione em um ambiente de teste sem ter o código real de LinkedBinaryTree:
# Você precisaria da sua LinkedBinaryTree real. Vamos usar uma definição mock para evitar erros.
class LinkedBinaryTree:
    """Mockup simplificado para simular a herança."""
    class Position:
        """Classe Position base (vazia, apenas para herança)."""
        pass

    def __init__(self):
        self._root = None
        self._size = 0

    def root(self):
        return self._root

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    # Métodos necessários para TreeMap (mocks simplificados)
    def _validate(self, p):
        return p

    def left(self, p):
        # A árvore real implementaria a lógica para encontrar o filho esquerdo
        return None

    def right(self, p):
        # A árvore real implementaria a lógica para encontrar o filho direito
        return None

    def parent(self, p):
        # A árvore real implementaria a lógica para encontrar o pai
        return None
    
    # Métodos de alteração necessários para __setitem__ e delete
    def _add_root(self, element):
        # Implementação real adiciona a raiz
        self._size += 1
        return self.Position() # Retorna uma Position mock

    def _add_left(self, p, element):
        # Implementação real adiciona à esquerda
        self._size += 1
        return self.Position() # Retorna uma Position mock

    def _add_right(self, p, element):
        # Implementação real adiciona à direita
        self._size += 1
        return self.Position() # Retorna uma Position mock

    def _replace(self, p, element):
        # Implementação real troca o elemento
        pass
    
    def _delete(self, p):
        # Implementação real deleta e manipula a estrutura
        self._size -= 1
        pass

# ---------------------- 1. Classe Base do Mapa (MapBase) ----------------------

class MapBase(collections.abc.MutableMapping):
    """Classe base abstrata para implementações de mapas. 
    Herdada de collections.abc.MutableMapping para obter métodos de mapa padrão."""

    class _Item:
        """Classe leve para armazenar um par chave-valor."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            """Permite a comparação baseada apenas na chave."""
            return self._key < other._key

        def __repr__(self):
            return '({0},{1})'.format(self._key, self._value)

    def __init__(self):
        """Cria um novo mapa (MapBase não armazena dados; subclasses o farão)."""
        pass
    
    # Métodos abstratos exigidos por MutableMapping (Implementados em TreeMap)
    # def __getitem__(self, k): raise NotImplementedError()
    # def __setitem__(self, k, v): raise NotImplementedError()
    # def __delitem__(self, k): raise NotImplementedError()
    # def __len__(self): raise NotImplementedError()
    # def __iter__(self): raise NotImplementedError()

# ---------------------- 2. Implementação da TreeMap ----------------------

class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree."""

    # ---------------------- override Position Class ----------------------
    class Position(LinkedBinaryTree.Position):
        """Posição aninhada na árvore para acessar convenientemente a chave e o valor."""
        def key(self):
            """Return key of map's key-value pair."""
            return self.element()._key

        def value(self):
            """Return value of map's key-value pair."""
            return self.element()._value

    # Para fins de TreeMap, renomeamos a classe _Item de MapBase
    _Item = MapBase._Item

    # Adicionando hooks de rebalanceamento (vazios, a serem preenchidos por AVL/Splay Tree)
    def _rebalance_insert(self, p): pass
    def _rebalance_delete(self, p): pass
    def _rebalance_access(self, p): pass

    # ---------------------- nonpublic utilities ----------------------
    def _subtree_search(self, p, k):
        """Return Position of p's subtree having key k, or last node searched."""
        if k == p.key():
            return p    # found match
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k) # search left subtree
            else:
                return p # unsuccessful search, p is the neighbor
        else: # k > p.key()
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k) # search right subtree
            else:
                return p # unsuccessful search, p is the neighbor

    def _subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p."""
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk) # keep walking left
        return walk

    def _subtree_last_position(self, p):
        """Return Position of last item in subtree rooted at p."""
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk) # keep walking right
        return walk

    # ---------------------- public utilities ----------------------
    def first(self):
        """Return the first Position in the tree (or None if empty)."""
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        """Return the last Position in the tree (or None if empty)."""
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        """Return the Position just before p in the natural order."""
        self._validate(p)
        if self.left(p) is not None:
            return self._subtree_last_position(self.left(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        """Return the Position just after p in the natural order."""
        self._validate(p)
        if self.right(p) is not None:
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        """Return position with key k, or else neighbor (or None if empty)."""
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p) 
            return p

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p) 
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
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

    def __iter__(self):
        """Generate an iteration of all keys in the map in order."""
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        """Remove the item at given Position."""
        self._validate(p)
        if self.left(p) is not None and self.right(p) is not None: # p has two children
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())
            p = replacement
        # now p has at most one child
        parent = self.parent(p)
        self._delete(p) # inherited from LinkedBinaryTree
        self._rebalance_delete(parent) 

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)
                return 
            self._rebalance_access(p) 
        raise KeyError('*Key Error: ' + repr(k))

    def find_min(self):
        """Return (key,value) pair with minimum key (or None if empty)."""
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())

    def find_ge(self, k):
        """Return (key,value) pair with least key greater than or equal to k."""
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.after(p) 
            return (p.key(), p.value()) if p is not None else None

    def find_range(self, start, stop):
        """Iterate all (key,value) pairs such that start <= key < stop."""
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)

# --------------------------------------------------------------------------------

# TESTES:

# --- Estruturas de Suporte Simplificadas para Teste (Itens, Posição e Mock) ---

class Item:
    """Um item simples para armazenar chave e valor."""
    def __init__(self, key, value):
        self._key = key
        self._value = value
    def __repr__(self):
        return f"({self._key}: {self._value})"

class Position:
    """Simula a Position retornada pela árvore (usada no Mock)."""
    def __init__(self, key, value):
        self._item = Item(key, value)
    def key(self):
        return self._item._key
    def value(self):
        return self._item._value
    def element(self):
        return self._item

class MockTreeMap:
    """Mockup simplificado da TreeMap com foco na busca e iteração."""
    def __init__(self):
        self._data = {}
        self._root_key = None
        self._is_empty = True

    def is_empty(self):
        return not self._data # Retorna True se _data está vazia

    def root(self):
        # Retorna a "posição" da raiz (simulada)
        return self._data.get(self._root_key)

    def _subtree_search(self, p, k):
        """Mock: Se a chave existe, retorna. Senão, retorna um Position que simula o nó 'vizinho'."""
        if k in self._data:
            return self._data[k]
        
        # Mocking do comportamento de busca: se não encontra, retorna o nó vizinho/último
        # Aqui, apenas retornamos uma posição com a chave k para que __setitem__ crie um novo.
        # Isso é uma simulação bem simplificada, mas suficiente para testar __setitem__ e __getitem__.
        
        # Para simular o nó vizinho, procuramos a chave mais próxima (inferior)
        # Se for um teste de inserção (como em __setitem__), ele usará p.key() para decidir.
        
        # Mock de um nó "próximo" (simplesmente retorna uma Position mockada com a chave)
        # Para que __setitem__ funcione, precisamos de um 'p' cuja chave seja diferente.
        
        # Encontra a chave mais próxima (simula o nó folha que seria o pai)
        closest_key = None
        for key in sorted(self._data.keys()):
            if key < k:
                closest_key = key
            else: # Primeira chave maior ou igual
                if closest_key is None: # Se k é menor que o mínimo
                    closest_key = key
                break
        
        if closest_key is None and self._data: # Se o mapa não está vazio, deve haver um 'pai' (último nó visitado)
             return self._data[max(self._data.keys())] # Retorna o máximo como fallback 
        
        return self._data.get(closest_key) or Position(k, None) # Usa o mais próximo ou mock simples

    # Métodos que a TreeMap real usaria (simulados)
    def _add_root(self, item):
        self._data[item._key] = Position(item._key, item._value)
        self._root_key = item._key
        return self._data[item._key]
        
    def _add_left(self, p, item):
        # Apenas adiciona ao dict para simular a inserção
        self._data[item._key] = Position(item._key, item._value)
        return self._data[item._key]
        
    def _add_right(self, p, item):
        # Apenas adiciona ao dict para simular a inserção
        self._data[item._key] = Position(item._key, item._value)
        return self._data[item._key]
        
    def _rebalance_access(self, p): pass
    def _rebalance_insert(self, p): pass
    
    def first(self):
        keys = sorted(self._data.keys())
        return self._data[keys[0]] if keys else None
    
    def after(self, p):
        keys = sorted(self._data.keys())
        if not keys: return None
        try:
            current_index = keys.index(p.key())
            if current_index + 1 < len(keys):
                return self._data[keys[current_index + 1]]
            else:
                return None
        except ValueError:
            return None # Não encontrado

# -----------------------------------------------------

# --- A Implementação dos Métodos Mágicos em MockTreeMap ---

class TreeMapTest(MockTreeMap):
    """Implementa os métodos mágicos usando a MockTreeMap como base. 
    Nota: Esses métodos são cópias exatas do TreeMap real para fins de teste."""
    
    def __getitem__(self, k):
        """Retorna valor associado à chave k."""
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p) 
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        """Atribui valor v à chave k, sobrescrevendo se existente."""
        if self.is_empty():
            leaf = self._add_root(Item(k,v)) 
        else:
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                # Chave encontrada: atualiza o valor
                p.element()._value = v 
                self._rebalance_access(p) 
                return
            else:
                # Chave não encontrada: insere novo nó
                item = Item(k,v)
                # O Mock não implementa _add_left/_add_right baseados em p, 
                # apenas em k < p.key() para fins de teste de fluxo
                if k < p.key():
                    leaf = self._add_left(p, item)
                else:
                    leaf = self._add_right(p, item)
                self._rebalance_insert(leaf) 

    def __iter__(self):
        """Gera uma iteração de todas as chaves no mapa em ordem."""
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

### 3. Demonstração dos Métodos

if __name__ == "__main__":
    
    mapa_bst = TreeMapTest()
    print("Início do Teste de TreeMap")
    print("-" * 30)

    # ------------------------------------------------
    # AÇÃO 1: __setitem__ (Inserir/Adicionar)
    # ------------------------------------------------
    print("1. Teste de Inserção (__setitem__):")
    mapa_bst[50] = "Cinquenta"
    mapa_bst[20] = "Vinte"
    mapa_bst[70] = "Setenta"
    mapa_bst[10] = "Dez"
    mapa_bst[60] = "Sessenta"
    
    print(f"Chaves inseridas (desordenadas no dict mock): {list(mapa_bst._data.keys())}")
    
    # AÇÃO 2: __setitem__ (Atualizar)
    mapa_bst[20] = "Vinte e Atualizado"
    print("Valor de 20 atualizado para 'Vinte e Atualizado'.")

    # ------------------------------------------------
    # AÇÃO 3: __getitem__ (Acesso)
    # ------------------------------------------------
    print("\n2. Teste de Acesso (__getitem__):")
    
    valor_50 = mapa_bst[50]
    valor_20 = mapa_bst[20]
    
    print(f"mapa_bst[50] -> {valor_50}")
    print(f"mapa_bst[20] -> {valor_20}")
    
    # Teste de chave inexistente (deve lançar KeyError)
    try:
        mapa_bst[99]
    except KeyError as e:
        print(f"mapa_bst[99] -> Capturou exceção: {e}")

    # ------------------------------------------------
    # AÇÃO 4: __iter__ (Iteração)
    # ------------------------------------------------
    print("\n3. Teste de Iteração (__iter__):")
    
    print("Iterando sobre as chaves em ordem (In-order traversal simulado):")
    for chave in mapa_bst:
        # Internamente, usa __iter__, first() e after()
        print(f"  Chave: {chave}")
        
    print(f"Chaves em lista (ordem correta, simulada): {list(mapa_bst)}")
    
    print("-" * 30)
    print("Fim do Teste.")