from collections import deque

def palindromo(texto):
    texto = texto.replace(" ", "").lower()
    pilha = []
    fila = deque()

    for c in texto:
        pilha.append(c)
        fila.append(c)

    while pilha:
        if pilha.pop() != fila.popleft():
            return False

    return True

palavra = input("Digite uma palavra: ")
if palindromo(palavra):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
