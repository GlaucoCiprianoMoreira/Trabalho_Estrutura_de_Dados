def recursive_pop(stack):
    if not stack:
        return
    stack.pop()
    recursive_pop(stack)


if __name__ == "__main__": 
    pilha = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Pilha antes de esvaziar:", pilha)
    recursive_pop(pilha)
    print("Pilha após esvaziar:", pilha)
