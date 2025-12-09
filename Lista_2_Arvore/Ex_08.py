class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def transformar_arvore_soma_subarvores(raiz: NoArvore) -> int:
    """
    Substitui o valor de cada nó pela soma dos elementos em suas subárvores esquerda e direita.
    
    Retorna a soma total (antiga) da subárvore para o nó pai.
    
    Complexidade Temporal: O(N), onde N é o número de nós.
    """
    
    # 1. Caso Base: Nó Nulo
    if raiz is None:
        return 0
    # 2. Pós-Ordem (Post-order): Chamada Recursiva
    soma_sub_esq = transformar_arvore_soma_subarvores(raiz.esquerda)
    # Obtém a soma total da subárvore direita (incluindo seus nós originais)
    soma_sub_dir = transformar_arvore_soma_subarvores(raiz.direita)
    # 3. Processamento do Nó Atual
    valor_original = raiz.valor
    # 4. Substituição do Valor do Nó
    novo_valor = soma_sub_esq + soma_sub_dir
    raiz.valor = novo_valor
    # 5. Retorno para o Nó Pai (Passo Crucial)
    return valor_original + soma_sub_esq + soma_sub_dir

def imprimir_pre_ordem(raiz: NoArvore):
    if raiz:
        print(raiz.valor, end=" ")
        imprimir_pre_ordem(raiz.esquerda)
        imprimir_pre_ordem(raiz.direita)

def imprimir_arvore(raiz: NoArvore, nome: str):
    print(f"\n--- {nome} (Pré-Ordem): ---")
    if raiz is None:
        print("Árvore Vazia.")
    else:
        imprimir_pre_ordem(raiz)
        print() # Nova linha
        
if __name__ == '__main__':
    
    # --- 1. Construindo a Árvore Original (Baseada na Imagem) ---
    # Estrutura (Valores Originais):
    #       1
    #     /   \
    #    2     3
    #   /     / \
    #  4     5   6
    #       / \
    #      7   8
    
    raiz_original = NoArvore(1)
    raiz_original.esquerda = NoArvore(2)
    raiz_original.direita = NoArvore(3)
    
    raiz_original.esquerda.esquerda = NoArvore(4)
    
    raiz_original.direita.esquerda = NoArvore(5)
    raiz_original.direita.direita = NoArvore(6)
    
    raiz_original.direita.esquerda.esquerda = NoArvore(7)
    raiz_original.direita.esquerda.direita = NoArvore(8)
    
    imprimir_arvore(raiz_original, "Árvore Original")
    # Saída esperada: 1 2 4 3 5 7 8 6

    print("\n--- Transformando a Árvore ---")
    print("Substituindo o valor de cada nó pela soma de todos os elementos em suas subárvores.")

    soma_total_original = transformar_arvore_soma_subarvores(raiz_original)
    print(f"Soma total da Árvore Original (retorno da função): {soma_total_original}")
    imprimir_arvore(raiz_original, "Árvore Transformada")