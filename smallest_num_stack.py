def find_smallest_number(stack):
    if not stack:
        return None
    smallest = stack.pop()
    if stack:
        temp = find_smallest_number(stack)
        if temp and temp < smallest:
            smallest = temp
    stack.append(smallest)
    return smallest

stack = list(map(int, input("Enter the stack elements: ").split()))
smallest_number = find_smallest_number(stack)
if smallest_number is not None:
    print("Smallest number in the stack:", smallest_number)
else:
    print("Stack is empty.")
