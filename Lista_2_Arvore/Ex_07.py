class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def encontrar_ancestrais(raiz: NoArvore, no_alvo_valor: int, caminho_ancestrais: list) -> bool:
    """
    Encontra e armazena os ancestrais de um nó específico.

    Retorna True se o nó alvo for encontrado na subárvore atual, False caso contrário.
    """
    # 1. Caso Base 1: Nó Nulo
    if raiz is None:
        return False
    # 2. Caso Base 2: Nó Alvo Encontrado
    if raiz.valor == no_alvo_valor:
        return True
    # 3. Processo de "Descida" (Adicionar ao Caminho)
    caminho_ancestrais.append(raiz.valor)
    # 4. Chamada Recursiva
    if encontrar_ancestrais(raiz.esquerda, no_alvo_valor, caminho_ancestrais):
        return True
    if encontrar_ancestrais(raiz.direita, no_alvo_valor, caminho_ancestrais):
        return True
    # 5. Backtracking: (Remove do Caminho)
    caminho_ancestrais.pop()
    # Se retornou False de ambas as chamadas e fez backtracking, retorna False.
    return False

def imprimir_ancestrais(raiz: NoArvore, no_alvo_valor: int):
    """Função wrapper para inicializar e imprimir o resultado."""
    ancestrais = []
    
    # Inicia a busca
    encontrado = encontrar_ancestrais(raiz, no_alvo_valor, ancestrais)
    
    print(f"Ancestrais do Nó com valor {no_alvo_valor}")
    if encontrado:
        if not ancestrais:
            print(f"O nó {no_alvo_valor} é a raiz. Não possui ancestrais.")
        else:
            print(" -> ".join(map(str, ancestrais)))
    else:
        print(f"O nó com valor {no_alvo_valor} não foi encontrado na árvore.")

if __name__ == "__main__":
    # Construindo a árvore de exemplo:
    #
    #         1
    #        / \
    #       /   \
    #      2     3
    #     / \   / \
    #    4   5 6   7
    #         /     \
    #        8       9
    #
    
    raiz = NoArvore(1)
    raiz.esquerda = NoArvore(2)
    raiz.direita = NoArvore(3)
    raiz.esquerda.esquerda = NoArvore(4)
    raiz.esquerda.direita = NoArvore(5)
    raiz.direita.esquerda = NoArvore(6)
    raiz.direita.direita = NoArvore(7)
    raiz.direita.esquerda.esquerda = NoArvore(8)
    raiz.direita.direita.direita = NoArvore(9)

    # Testes de impressão de ancestrais
    imprimir_ancestrais(raiz, 8)  # Deve mostrar: 1 -> 3 -> 6
    imprimir_ancestrais(raiz, 5)  # Deve mostrar: 1 -> 2
    imprimir_ancestrais(raiz, 1)  # Deve indicar que é a raiz
    imprimir_ancestrais(raiz, 10) # Deve indicar que o nó não foi encontrado