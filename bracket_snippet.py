# Q8. Write a program to check if all the brackets are closed in a given code snippet.

def check_brackets(code):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    for char in code:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                return False
    return len(stack) == 0

code_snippet = input("Enter the code snippet: ")
if check_brackets(code_snippet):
    print("All brackets are closed.")
else:
    print("Not all brackets are closed.")