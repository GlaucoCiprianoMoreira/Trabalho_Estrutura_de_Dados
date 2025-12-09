def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def apply_op(op, b, a):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ValueError("Divisão por zero não permitida")
        return a // b

def evaluate_expression(expression):
    tokens = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isspace():
            i += 1
            continue
        elif char.isdigit():
            num_str = ''
            while i < len(expression) and expression[i].isdigit():
                num_str += expression[i]
                i += 1
            tokens.append(int(num_str))
            continue
        elif char in ['+', '-', '*', '/', '(', ')']:
            tokens.append(char)
        
        i += 1

    values = []
    ops = []

    for token in tokens:
        if isinstance(token, int):
            values.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops[-1] != '(':
                op = ops.pop()
                val2 = values.pop()
                val1 = values.pop()
                values.append(apply_op(op, val2, val1))
            ops.pop() # Pop '('
        else: # Operador
            while (len(ops) != 0 and ops[-1] != '(' and 
                   precedence(ops[-1]) >= precedence(token)):
                op = ops.pop()
                val2 = values.pop()
                val1 = values.pop()
                values.append(apply_op(op, val2, val1))
            ops.append(token)

    while len(ops) != 0:
        op = ops.pop()
        val2 = values.pop()
        val1 = values.pop()
        values.append(apply_op(op, val2, val1))

    return values[0]

if __name__ == "__main__":
    test_expression = "10 + 2 * (6 - 4) / 2"
    result = evaluate_expression(test_expression)
    print(f"Expressão: {test_expression}")
    print(f"Resultado: {result}")
    
    test_expression_2 = "3 + 4 * 2 / (1 - 5) + 6"
    result_2 = evaluate_expression(test_expression_2)
    print(f"Expressão: {test_expression_2}")
    print(f"Resultado: {result_2}")