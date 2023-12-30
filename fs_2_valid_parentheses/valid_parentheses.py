def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False

        >>> valid_parentheses("()))((()")
        False

        >>> valid_parentheses("(())))(())((()")
        False
    """
    check = 0
    for char in parens:
        if char == "(":
            check += 1
        elif char == ")":
            check -= 1
        if check < 0:
            return False
    return check == 0 and len(parens) % 2 == 0