class Node:
    """Representa um nó na Árvore."""
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key)

def get_height(node):
    """Retorna a altura do nó (-1 para None)."""
    if node is None:
        return -1
    return 1 + max(get_height(node.left), get_height(node.right))

def get_balance_factor(node):
    """Calcula o Fator de Balanceamento (Altura Direita - Altura Esquerda)."""
    if node is None:
        return 0
    return get_height(node.right) - get_height(node.left)

# --------------------------------------------------
# MÉTODOS DE ROTAÇÃO AVL
# --------------------------------------------------

def rotate_left(z):
    """Executa a rotação simples à esquerda (Left-Left Case)."""
    y = z.right  # y é o novo nó raiz
    T2 = y.left
    
    # Executa a rotação
    y.left = z
    z.right = T2
    
    # Não precisamos recomputar FB/Altura aqui, pois serão recomputados pelo chamador
    return y

# Funções rotate_right e rotate_left_right/rotate_right_left seriam necessárias 
# para um sistema AVL completo.

# --------------------------------------------------
# MÉTODOS DE REMOÇÃO E BALANCEAMENTO
# --------------------------------------------------

def find_min(node):
    """Encontra o nó com a chave mínima na subárvore."""
    current = node
    while current.left is not None:
        current = current.left
    return current

def remove_bst(root, key):
    """Remove uma chave na BST, retornando a nova raiz e o nó removido."""
    if root is None:
        return root, None

    removed_node = None
    
    if key < root.key:
        root.left, removed_node = remove_bst(root.left, key)
    elif key > root.key:
        root.right, removed_node = remove_bst(root.right, key)
    else:
        # Nó a ser removido encontrado
        removed_node = root
        
        # Caso 1: Nó com 0 ou 1 filho
        if root.left is None:
            return root.right, removed_node
        elif root.right is None:
            return root.left, removed_node
        
        # Caso 2: Nó com 2 filhos
        # Encontra o sucessor in-order (mínimo na subárvore direita)
        temp = find_min(root.right)
        
        # Copia o conteúdo do sucessor para este nó
        root.key = temp.key
        
        # Remove o sucessor (agora o problema é tratar a remoção na subárvore direita)
        root.right, _ = remove_bst(root.right, temp.key)
        
    return root, removed_node

def check_avl_and_rebalance(root):
    """Verifica e rebalanceia o nó se necessário."""
    if root is None:
        return root

    # 1. Recalcula o FB
    fb = get_balance_factor(root)

    # 2. Rebalanceia se |FB| > 1
    if fb > 1:
        # Desbalanceamento à Direita (R-L ou R-R)
        if get_balance_factor(root.right) >= 0:
            # Caso Direita-Direita (R-R): Rotação Simples à Esquerda (Left-Left Case)
            print(f"** Rotação Simples à Esquerda necessária no nó {root.key} **")
            return rotate_left(root)
        # else:
            # Caso Direita-Esquerda (R-L): Rotação Dupla
            # root.right = rotate_right(root.right)
            # return rotate_left(root)
            
    elif fb < -1:
        # Desbalanceamento à Esquerda (L-L ou L-R)
        # ... Rotações à direita seriam implementadas aqui
        pass
        
    return root

def print_tree_structure(root):
    """Imprime a árvore em formato vertical com FB e Altura."""
    if root is None:
        return

    def _print_tree(node, level=0, prefix="Root: "):
        if node is not None:
            fb = get_balance_factor(node)
            h = get_height(node)
            
            print(" " * (level * 4) + prefix + f"[{node.key}] (FB: {fb}, H: {h})")
            
            if node.right is not None:
                _print_tree(node.right, level + 1, "R--- ")
            if node.left is not None:
                _print_tree(node.left, level + 1, "L--- ")

    _print_tree(root)
    print("-" * 40)

# =================================================================
# MONTAGEM E EXECUÇÃO
# =================================================================

# Estrutura Inicial (Cenário que força Rotação Simples à Esquerda após remover 62):
# Nó 60 desbalanceará para +2 após a remoção de 62, e 70 tem FB >= 0.

# Inicialização dos nós folhas/internos
node_62 = Node(62)
node_75 = Node(75)
node_70 = Node(70, left=node_62, right=node_75) # FB(70) = 0
node_60 = Node(60, right=node_70)               # FB(60) = +2
node_90 = Node(90)
node_80 = Node(80, left=node_60, right=node_90) # FB(80) = +1
node_40 = Node(40)
node_20 = Node(20)
node_30 = Node(30, left=node_20, right=node_40) # FB(30) = 0
root_initial = Node(50, left=node_30, right=node_80) # FB(50) = +1

print("--- ÁRVORE AVL INICIAL (Pré-Remoção de 62) ---")
print_tree_structure(root_initial)

# 1. Remoção da Chave 62
CHAVE_REMOVER = 62
print(f"--- Removendo a Chave {CHAVE_REMOVER} ---")

# Removemos 62 (nó folha, filho esquerdo de 70)
root_initial.right.left.right.left, _ = remove_bst(root_initial.right.left.right.left, CHAVE_REMOVER)

print("\n--- ÁRVORE APÓS REMOÇÃO (Desbalanceada em 60) ---")
print_tree_structure(root_initial)

# 2. Verificação e Rebalanceamento (Subindo a partir do pai do nó removido, 70)

# Rebalanceamento no Nó 70 (pai de 62):
root_initial.right.left.right = check_avl_and_rebalance(root_initial.right.left.right) # Nó 70

# Rebalanceamento no Nó 60 (avô de 62):
root_initial.right.left = check_avl_and_rebalance(root_initial.right.left) # Nó 60
# A rotação altera a estrutura: 70 é agora o novo filho esquerdo de 80

# Rebalanceamento no Nó 80:
root_initial.right = check_avl_and_rebalance(root_initial.right) # Nó 80

# Rebalanceamento na Raiz 50:
root_final = check_avl_and_rebalance(root_initial)

print("\n--- ÁRVORE AVL RESULTANTE (Após Rotação) ---")
print_tree_structure(root_final)