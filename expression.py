# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def postfix_to_prefix(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for char in expression:
        if char not in operators:
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix = char + operand1 + operand2
            stack.append(prefix)

    return stack.pop()

expression = input("Enter a postfix expression: ")

prefix_expression = postfix_to_prefix(expression)


print("Prefix expression:", prefix_expression)
