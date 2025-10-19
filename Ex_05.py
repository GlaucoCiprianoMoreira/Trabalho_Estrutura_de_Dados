
def inverte_lista(lista):
    pilha = []
    for i in lista:
        pilha.append(i)
    lista_invertida = []
    while pilha:
        lista_invertida.append(pilha.pop())
    return lista_invertida

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    print("Lista original:", l)
    l = inverte_lista(l)
    print("Lista invertida:", l)