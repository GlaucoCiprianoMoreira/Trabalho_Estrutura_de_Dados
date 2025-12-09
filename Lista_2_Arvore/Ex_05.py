class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def verificar_arvore_soma_recursiva(raiz: NoArvore):
    if raiz is None:
        return (True, 0)

    if raiz.esquerda is None and raiz.direita is None:
        return (True, raiz.valor)

    esq_valido, soma_esq = verificar_arvore_soma_recursiva(raiz.esquerda)

    dir_valido, soma_dir = verificar_arvore_soma_recursiva(raiz.direita)
    
    valido_atual = esq_valido and dir_valido and (raiz.valor == (soma_esq + soma_dir))

    soma_total_atual = raiz.valor + soma_esq + soma_dir
    
    return (valido_atual, soma_total_atual)

def e_arvore_soma(raiz: NoArvore) -> bool:
    """Função wrapper para obter apenas o resultado booleano."""
    valido, _ = verificar_arvore_soma_recursiva(raiz)
    return valido


if __name__ == "__main__":
    # --- ÁRVORE 1: Exemplo Válido de Árvore Soma ---
    print("--- Construindo Árvore Soma Válida ---")
    raiz_a = NoArvore(26)
    raiz_a.esquerda = NoArvore(10)
    raiz_a.direita = NoArvore(3)
    raiz_a.esquerda.esquerda = NoArvore(4)
    raiz_a.esquerda.direita = NoArvore(6)
    raiz_a.direita.direita = NoArvore(3)

    # --- ÁRVORE 2: Exemplo Inválido de Árvore Soma ---
    print("--- Construindo Árvore Soma Inválida ---")
    raiz_b = NoArvore(10)
    raiz_b.esquerda = NoArvore(5)
    raiz_b.direita = NoArvore(3)

    print("\n--- TESTES DE ÁRVORE SOMA ---")
    resultado_a = e_arvore_soma(raiz_a)
    print(f"A árvore A é uma Árvore Soma? {resultado_a}")

    resultado_b = e_arvore_soma(raiz_b)
    print(f"A árvore B é uma Árvore Soma? {resultado_b}")