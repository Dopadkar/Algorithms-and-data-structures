import stack

def is_braces_sequences_correct(s):
    """
    Проверяет корректность скобочной последовательности из куглых и квадратных скобок.
    >>> is_braces_sequences_correct('(([()]))[]')
    True
    >>> is_braces_sequences_correct('[(])')
    False
    >>> is_braces_sequences_correct('(')
    False
    >>> is_braces_sequences_correct(']')
    False
    """
    braces = '()[]'
    for brace in s:
        if brace not in braces:
            continue
        if brace in '([':
            stack.push(brace)
        else:
            assert brace in ')]', 'Oups! I expect close brace: ' + str(brace)
            if stack.is_empty():
                return False
            left = stack.pop()
            assert left in '([', 'Oups! I expect open brace: ' + str(brace)
            if left == "(":
                right = ")" 
            if left == "[":
                right = "]"
            if right != brace:
                return False
    return stack.is_empty()

    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    
