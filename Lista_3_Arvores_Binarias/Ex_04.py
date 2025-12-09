class Node:
    """Representa um nó na Árvore de Busca Binária (BST)."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)

class BST:
    """Implementa a Árvore de Busca Binária."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insere uma nova chave na BST."""
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if key < current.key:
                # Vai para a esquerda
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif key > current.key:
                # Vai para a direita
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                # Chave já existe (ignora inserção)
                return

    def print_tree(self):
        """Imprime a estrutura da árvore."""
        if self.root is None:
            print("Árvore vazia.")
            return
        
        # Função auxiliar recursiva para impressão
        def _print_tree(node, level=0, prefix="Root: "):
            if node is not None:
                # Imprime a linha atual: prefixo (conexão) + nível de indentação + chave
                print(" " * (level * 4) + prefix + str(node.key))
                
                # Chamada recursiva para o filho esquerdo
                if node.left is not None or node.right is not None:
                    # Se houver filho esquerdo, imprime 'L---' (Left)
                    _print_tree(node.left, level + 1, "L--- ")
                    # Se houver filho direito, imprime 'R---' (Right)
                    _print_tree(node.right, level + 1, "R--- ")

        _print_tree(self.root)
        print("-" * 30)


# =================================================================
# EXECUÇÃO E TESTE
# =================================================================

chaves = [30, 40, 24, 58, 48, 26, 11, 13]
bst = BST()

print("--- Demonstração de Inserção na BST ---")
print("-" * 30)

for i, chave in enumerate(chaves):
    print(f"Passo {i+1}: Inserindo a chave {chave}")
    bst.insert(chave)
    bst.print_tree()

print("FIM DA DEMONSTRAÇÃO.")