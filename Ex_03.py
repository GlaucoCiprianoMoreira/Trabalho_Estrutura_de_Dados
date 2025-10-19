def transfer(S, T):
    temp = []
    temp = S.copy()
    while temp:
        T.append(temp.pop())

if __name__ == "__main__": 
    S = [1, 2, 3, 4, 5]
    T = []

    transfer(S, T)

    print("Pilha S:", S)
    print("Pilha T:", T)