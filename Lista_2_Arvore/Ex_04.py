# A classe NoArvore representa um nó em uma LinkedBinaryTree
class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None # Link
        self.direita = None  # Link

def saoIdenticas(raiz1: NoArvore, raiz2: NoArvore) -> bool:
    """
    Verifica recursivamente se duas árvores binárias são idênticas.
    Complexidade Temporal: O(N), onde N é o número de nós na menor árvore.
    """

    # 1. Caso Base: Ambos os nós são NULOS (Links vazios).
    if raiz1 is None and raiz2 is None:
        return True
    # 2. Caso Base: Um nó é NULO e o outro não.
    if raiz1 is None or raiz2 is None:
        return False
    # 3. Comparação de Conteúdo: Os valores dos nós atuais são diferentes.
    if raiz1.valor != raiz2.valor:
        return False
    # 4. Chamada Recursiva: Se a estrutura e o conteúdo até aqui forem iguais,
    # verificamos as subárvores esquerda E direita. A identidade exige que
    # ambas as subárvores sejam idênticas.
    esquerda_identica = saoIdenticas(raiz1.esquerda, raiz2.esquerda)
    direita_identica = saoIdenticas(raiz1.direita, raiz2.direita)
    return esquerda_identica and direita_identica


if __name__ == "__main__":
    
    # --- ÁRVORE 1: Estrutura: 10 -> (5, 15) ---
    print("--- Construindo Árvore A ---")
    raiz_a = NoArvore(10)
    raiz_a.esquerda = NoArvore(5)
    raiz_a.direita = NoArvore(15)
    # Nó 5 possui filhos nulos
    # Nó 15 possui filhos nulos
    
    
    # --- ÁRVORE 2: Cópia Idêntica ---
    print("--- Construindo Árvore B (Cópia Idêntica a A) ---")
    raiz_b = NoArvore(10)
    raiz_b.esquerda = NoArvore(5)
    raiz_b.direita = NoArvore(15)
    
    # --- ÁRVORE 3: Estrutura Diferente (Conteúdo Diferente) ---
    print("--- Construindo Árvore C (Não Idêntica a A) ---")
    raiz_c = NoArvore(10)
    raiz_c.esquerda = NoArvore(5)
    raiz_c.direita = NoArvore(20) # Valor diferente (20 vs 15)
    
    # --- ÁRVORE 4: Estrutura Diferente (Falta Nó) ---
    print("--- Construindo Árvore D (Não Idêntica a A) ---")
    raiz_d = NoArvore(10)
    raiz_d.esquerda = NoArvore(5)
    # raiz_d.direita = None (Nó 15 está faltando)
    
    print("\n--- TESTES DE IDENTIDADE ---")
    
    # Teste 1: Idênticas
    resultado1 = saoIdenticas(raiz_a, raiz_b)
    print(f"Árvore A vs Árvore B (Idênticas): {resultado1}")
    
    # Teste 2: Conteúdo Diferente
    resultado2 = saoIdenticas(raiz_a, raiz_c)
    print(f"Árvore A vs Árvore C (Conteúdo Diferente): {resultado2}")
    
    # Teste 3: Estrutura Diferente (Falta Nó)
    resultado3 = saoIdenticas(raiz_a, raiz_d)
    print(f"Árvore A vs Árvore D (Estrutura Diferente): {resultado3}")
    
    # Teste 4: Árvores Vazias
    resultado4 = saoIdenticas(None, None)
    print(f"Árvore Vazia vs Árvore Vazia: {resultado4}")