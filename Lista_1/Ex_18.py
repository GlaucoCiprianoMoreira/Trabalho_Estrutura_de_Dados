class No:
    def __init__(self, dado=None):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionar(self, dado):
        novo_no = No(dado)
        if not self.cabeca:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def para_lista(self):
        elementos = []
        atual = self.cabeca
        while atual:
            elementos.append(atual.dado)
            atual = atual.proximo
        return elementos

def separar_listas(lista_original):
    lista_positivos = ListaEncadeada()
    lista_negativos = ListaEncadeada()

    atual = lista_original.cabeca
    while atual:
        if atual.dado is not None:
            if atual.dado > 0:
                lista_positivos.adicionar(atual.dado)
            elif atual.dado < 0:
                lista_negativos.adicionar(atual.dado)
        atual = atual.proximo

    return lista_positivos, lista_negativos

if __name__ == '__main__':
    lista_original = ListaEncadeada()
    elementos = [1, -5, 10, -3, 7, -20, 0, 15]
    for e in elementos:
        lista_original.adicionar(e)

    lista_positivos, lista_negativos = separar_listas(lista_original)

    print(lista_original.para_lista())
    print(lista_positivos.para_lista())
    print(lista_negativos.para_lista())