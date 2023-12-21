"""module with functions used for checking brace sequences
Implements two functions:
is_cbs(list) -> bool
and 
need_to_move(list) -> int
all work on a sequence of characters
"""
def is_cbs(sequence) -> bool:
    """returns a bool that has the sequence's correctness
    checks ONLY the correctness of BRACES in a sequence of chars
    """
    stack = []
    for char in sequence:
        if char not in "()":
            continue
        if len(stack) == 0:
            stack.append(char)
        else:
            if stack[-1] == '(' and char == ')':
                stack.pop()
            else:
                stack.append(char)
    if len(stack) == 0:
        return True
    return False

def need_to_move(sequence) -> int:
    """returns the amount of moves* needed to fix the sequence to a cbs
    *moves - as in addition of characters or their movement
    """
    stack = []
    for char in sequence:
        if len(stack) == 0:
            stack.append(char)
        else:
            if stack[-1] == '(' and char == ')':
                stack.pop()
            else:
                stack.append(char)
    a = stack.count('(')
    b = stack.count(')')
    return max(a,b)
