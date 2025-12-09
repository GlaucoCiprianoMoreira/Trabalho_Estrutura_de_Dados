class Node:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
    def conta_nos_recursivo(self, no_atual):
        if no_atual is None:
            return 0

        else:
            return 1 + self.conta_nos_recursivo(no_atual.proximo)

    def obter_tamanho(self):
        """Método wrapper para iniciar a contagem a partir da cabeça da lista."""
        return self.conta_nos_recursivo(self.cabeca)

lista = ListaEncadeada()

lista.cabeca = Node(10)
lista.cabeca.proximo = Node(20)
lista.cabeca.proximo.proximo = Node(30)
lista.cabeca.proximo.proximo.proximo = Node(40)

tamanho = lista.obter_tamanho()
print(f"O número de nós na lista é: {tamanho}")

lista_vazia = ListaEncadeada()
tamanho_vazio = lista_vazia.obter_tamanho()
print(f"O número de nós na lista vazia é: {tamanho_vazio}")