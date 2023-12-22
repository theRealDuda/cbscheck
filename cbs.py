"""module with functions used for checking brace sequences
Implements two functions:
is_cbs(list) -> bool
and 
need_to_move(list) -> int
all work on a sequence of characters
"""
def is_cbs(sequence) -> bool:
    """Check the input and returns its correctness

    Args:
        sequence (list): a sequence of characters

    Returns:
        bool: a boolean representing the sequences correctness
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
    """function used for finding the amount of moves 
    needed to turn a sequence into a correct one
    *moves - as in addition of characters or their movement
    Args:
        sequence (list): a sequence of characters

    Returns:
        int: the amount of moves needed
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
