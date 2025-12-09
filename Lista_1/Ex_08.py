def parenteses_bem_formados(expressao):
    pilha = []

    for caractere in expressao:
        if caractere == '(':
            pilha.append(caractere)
        elif caractere == ')':
            if not pilha:
                return False
            pilha.pop()

    return len(pilha) == 0

expressao = "(2 + 3) * (5 - (1 + 2))"

if parenteses_bem_formados(expressao):
    print("Os parênteses estão bem formados!")
else:
    print("Os parênteses NÃO estão bem formados.")
