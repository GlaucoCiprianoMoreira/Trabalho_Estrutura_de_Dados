class Node:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaCircular:
    def __init__(self):
        self.cabeca = None
    
    def adicionar_no_final(self, dado):
        novo_no = Node(dado)
        
        if self.cabeca is None:
            self.cabeca = novo_no
            novo_no.proximo = self.cabeca
        else:
            atual = self.cabeca
            while atual.proximo != self.cabeca:
                atual = atual.proximo
            
            atual.proximo = novo_no
            novo_no.proximo = self.cabeca

    def contar_nos(self):
        if self.cabeca is None:
            return 0

        contagem = 0
        atual = self.cabeca
        
        while True:
            contagem += 1
            atual = atual.proximo
            
            if atual == self.cabeca:
                break
                
        return contagem

lista = ListaCircular()
print(f"Contagem inicial (lista vazia): {lista.contar_nos()}")

lista.adicionar_no_final(10)
print(f"Contagem após 1 nó: {lista.contar_nos()}")

lista.adicionar_no_final(20)
lista.adicionar_no_final(30)
lista.adicionar_no_final(40)

total_nos = lista.contar_nos()
print(f"O número total de nós na lista circular é: {total_nos}")

lista_vazia = ListaCircular()
print(f"Contagem da lista vazia: {lista_vazia.contar_nos()}")