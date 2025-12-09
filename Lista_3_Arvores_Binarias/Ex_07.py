import sys

# Para evitar RecursionError em árvores profundas
sys.setrecursionlimit(2000)

class Node:
    """Nó da Árvore Rubro-Negra, mantendo a cor e a chave."""
    RED = True
    BLACK = False

    def __init__(self, key, parent=None, color=RED):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color

    def is_red(self):
        return self.color == self.RED

    def set_color(self, color):
        self.color = color

    def __str__(self):
        color_str = "R" if self.is_red() else "B"
        return f"[{self.key}]({color_str})"

class RedBlackTree:
    """Implementação da Árvore Rubro-Negra com Inserção."""

    def __init__(self):
        self.root = None

    # --- MÉTODOS DE ROTAÇÃO (Essenciais para Rebalanceamento) ---

    def _rotate_left(self, x):
        """Rotação Simples à Esquerda no nó x."""
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y
        return y # Retorna a nova raiz da subárvore

    def _rotate_right(self, x):
        """Rotação Simples à Direita no nó x."""
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x
        y.parent = x.parent
        
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        
        y.right = x
        x.parent = y
        return y # Retorna a nova raiz da subárvore

    # --- MÉTODO DE INSERÇÃO E REBALANCEAMENTO ---

    def insert(self, key):
        """Insere uma chave e rebalanceia a RB-Tree."""
        if self.root is None:
            self.root = Node(key, color=Node.BLACK) # Regra 2: Raiz é preta
            return
        
        # 1. Inserção como BST (novo nó é sempre VERMELHO)
        current = self.root
        parent = None
        while current is not None:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        
        new_node = Node(key, parent=parent, color=Node.RED) # Regra 5: Novo nó é vermelho
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
            
        # 2. Rebalanceamento (Consertar violações R-R)
        self._fix_violation(new_node)


    def _fix_violation(self, z):
        """Corrige a violação R-R subindo na árvore."""
        
        # O rebalanceamento é necessário apenas se o nó atual (z) for vermelho
        # e seu pai (p) também for vermelho.
        while z != self.root and z.parent.is_red():
            p = z.parent
            g = p.parent # Avô
            
            if g is None:
                # O pai (p) é a raiz, mas já deveria ser preto.
                # Se p é vermelho e g é None, p é a raiz e deve ser preto.
                p.set_color(Node.BLACK)
                break
            
            # Determina o tio (u)
            u = g.right if p == g.left else g.left
            
            if u is not None and u.is_red():
                # Caso 1: Tio Vermelho (Recolorimento)
                p.set_color(Node.BLACK)
                u.set_color(Node.BLACK)
                g.set_color(Node.RED)
                z = g # Propaga a violação para o avô (g)
            
            else:
                # Caso 2/3: Tio Preto (Rotação)
                
                # Caso 2: Triângulo (Zig-Zag): Ex: Left-Right (LR) ou Right-Left (RL)
                if (z == p.right and p == g.left) or (z == p.left and p == g.right):
                    if z == p.right and p == g.left:
                        self._rotate_left(p)
                        z = z.left # O novo 'z' (antigo p) será o ponto de partida para o Caso 3
                    else: # z == p.left and p == g.right
                        self._rotate_right(p)
                        z = z.right # O novo 'z' (antigo p) será o ponto de partida para o Caso 3
                    p = z.parent # Atualiza p para ser o novo pai (agora a linha)
                
                # Caso 3: Linha (Zig-Zig): Ex: Left-Left (LL) ou Right-Right (RR)
                p.set_color(Node.BLACK) # O pai (p) se torna preto
                g.set_color(Node.RED)   # O avô (g) se torna vermelho
                
                if z == p.left: # Left-Left (LL)
                    self._rotate_right(g)
                else: # Right-Right (RR)
                    self._rotate_left(g)

        # A raiz deve ser sempre preta (Regra 2)
        self.root.set_color(Node.BLACK)

    # --- MÉTODO DE IMPRESSÃO ---

    def print_tree(self):
        """Imprime a estrutura da árvore com cores."""
        if self.root is None:
            print("Árvore vazia.")
            return

        def _print_tree(node, level=0, prefix="Root: "):
            if node is not None:
                print(" " * (level * 4) + prefix + str(node))
                
                # Chamada recursiva para o filho direito
                if node.right is not None:
                    _print_tree(node.right, level + 1, "R--- ")
                
                # Chamada recursiva para o filho esquerdo
                if node.left is not None:
                    _print_tree(node.left, level + 1, "L--- ")

        _print_tree(self.root)
        print("-" * 50)


# =================================================================
# EXECUÇÃO E TESTE DA SEQUÊNCIA
# =================================================================

chaves = [5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1]
rbt = RedBlackTree()

print("--- Construção da Árvore Rubro-Negra (RB-Tree) ---")
print(f"Sequência de chaves: {chaves}\n")

for i, chave in enumerate(chaves):
    print(f"Passo {i+1}: Inserindo a chave {chave}")
    rbt.insert(chave)
    rbt.print_tree()

print("FIM DA CONSTRUÇÃO.")