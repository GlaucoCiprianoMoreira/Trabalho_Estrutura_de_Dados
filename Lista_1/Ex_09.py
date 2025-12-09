def is_operator(c):
    return c in ['+', '-', '*', '/', '^']

def prefix_to_infix(prefix_expr):
    stack = []
    for symbol in prefix_expr.split()[::-1]:
        if not is_operator(symbol):
            stack.append(symbol)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            new_expr = f"({op1} {symbol} {op2})"
            stack.append(new_expr)
    return stack[-1]

def prefix_to_postfix(prefix_expr):
    stack = []
    for symbol in prefix_expr.split()[::-1]:
        if not is_operator(symbol):
            stack.append(symbol)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            new_expr = f"{op1} {op2} {symbol}"
            stack.append(new_expr)
    return stack[-1]

if __name__ == "__main__":
    prefix = ("* + A B C")
    
    infix = prefix_to_infix(prefix)
    postfix = prefix_to_postfix(prefix)
    
    print("\nForma infixa  :", infix)
    print("Forma pós-fixa:", postfix)
