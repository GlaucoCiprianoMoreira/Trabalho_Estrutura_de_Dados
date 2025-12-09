class Node:
    """Representa um nó na Árvore."""
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key)

def get_height(node):
    """Retorna a altura do nó (0 para nó folha, -1 para None)."""
    if node is None:
        return -1
    # Altura é 1 + máximo da altura dos filhos
    return 1 + max(get_height(node.left), get_height(node.right))

def get_balance_factor(node):
    """Calcula o Fator de Balanceamento (Altura Direita - Altura Esquerda)."""
    if node is None:
        return 0
    return get_height(node.right) - get_height(node.left)

def insert_bst(root, key):
    """Insere uma chave em uma BST, retornando a nova raiz."""
    if root is None:
        return Node(key)
    
    if key < root.key:
        root.left = insert_bst(root.left, key)
    elif key > root.key:
        root.right = insert_bst(root.right, key)
    
    return root

def print_tree_structure(root):
    """Imprime a árvore em formato vertical com FB e Altura."""
    if root is None:
        return

    def _print_tree(node, level=0, prefix="Root: "):
        if node is not None:
            fb = get_balance_factor(node)
            h = get_height(node)
            
            # Imprime o nó com o FB e a Altura
            print(" " * (level * 4) + prefix + f"[{node.key}] (FB: {fb}, H: {h})")
            
            # Chamada recursiva para o filho direito (imprimido primeiro para visualização)
            if node.right is not None:
                _print_tree(node.right, level + 1, "R--- ")
            
            # Chamada recursiva para o filho esquerdo
            if node.left is not None:
                _print_tree(node.left, level + 1, "L--- ")

    _print_tree(root)
    print("-" * 40)

def check_avl_and_rotate(root):
    """
    Verifica se o nó está desbalanceado. 
    (Neste exercício, esta função apenas verificará e retornará a raiz,
    pois determinamos que não há rotação necessária.)
    """
    if root is None:
        return root

    # Verifica o FB do nó atual
    fb = get_balance_factor(root)
    
    # Se |FB| > 1, rotação seria necessária.
    if abs(fb) > 1:
        print(f"\n❌ Desbalanceamento detectado no nó {root.key} (FB: {fb}). Rotação necessária!")
        # A lógica real de rotação AVL (simples ou dupla) seria implementada aqui.
        # Por exemplo, se fb > 1 (desbalanceamento à direita):
        # if fb > 1 and get_balance_factor(root.right) < 0:
        #     # Caso Direita-Esquerda (Dupla Rotação)
        #     root.right = rotate_right(root.right)
        #     return rotate_left(root)
        # return rotate_left(root) # Caso Direita-Direita (Simples Rotação)
        
        # Como o exercício resultou em não precisar de rotação, paramos aqui.
        return root 
    
    return root

# =================================================================
# MONTAGEM E EXECUÇÃO
# =================================================================

# 1. Montagem da Árvore Inicial (Baseado na Figura 11.14b)
# Estrutura: Raiz 50, Filhos 30 e 80, Neto 60 (onde 52 será inserido), etc.
node_60 = Node(60)
node_90 = Node(90)
node_40 = Node(40)
node_20 = Node(20)

node_80 = Node(80, left=node_60, right=node_90)
node_30 = Node(30, left=node_20, right=node_40)
root_initial = Node(50, left=node_30, right=node_80)

print("--- Árvore AVL Inicial (Figura 11.14b) ---")
print_tree_structure(root_initial)

# 2. Inserção da Chave 52
CHAVE_INSERIR = 52
print(f"--- Inserindo a Chave {CHAVE_INSERIR} ---")

# Insere a chave 52 na BST
root_bst = insert_bst(root_initial, CHAVE_INSERIR)

# 3. Verificação do Balanceamento (Subindo a partir do nó inserido: 60, 80, 50)

# O nó 52 foi inserido como filho esquerdo de 60.
# Verificação no nó 60:
root_bst.right.left = check_avl_and_rotate(root_bst.right.left) 

# Verificação no nó 80:
root_bst.right = check_avl_and_rotate(root_bst.right)

# Verificação na Raiz 50:
root_final = check_avl_and_rotate(root_bst)

print("\n--- ÁRVORE AVL RESULTANTE ---")
print("Nenhuma rotação foi necessária.")
print_tree_structure(root_final)