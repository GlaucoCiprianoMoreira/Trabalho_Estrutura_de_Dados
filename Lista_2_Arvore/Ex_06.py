class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def caminho_auxiliar(no_atual: NoArvore, caminho_atual: list):
    # Caso Base 1: Nó nulo, retorna imediatamente.
    if no_atual is None:
        return
    # 1. Processo de "Descer": Adiciona o valor do nó atual ao caminho.
    caminho_atual.append(no_atual.valor)
    # 2. Caso Base 2: Nó Folha
    if no_atual.esquerda is None and no_atual.direita is None:
        # Imprime o caminho
        print(" -> ".join(map(str, caminho_atual)))
    else:
        # 3. Chamada Recursiva: Explora a esquerda e a direita.
        caminho_auxiliar(no_atual.esquerda, caminho_atual)
        caminho_auxiliar(no_atual.direita, caminho_atual)

    # 4. Backtracking:
    caminho_atual.pop()

def imprimir_caminhos_raiz_folha(raiz: NoArvore):
    """
    Inicia o processo de impressão dos caminhos da raiz para a folha.
    """
    if raiz is None:
        print("A árvore está vazia.")
        return
    caminho_inicial = []
    caminho_auxiliar(raiz, caminho_inicial)

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

    print("Caminhos da raiz para as folhas:")
    imprimir_caminhos_raiz_folha(raiz)