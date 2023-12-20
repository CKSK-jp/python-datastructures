def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped = ''
    for char in phrase:
        if char.lower() == to_swap.lower():
            if char.isupper():
                swapped += char.lower()
            elif char.islower():
                swapped += char.upper()
        else:
            swapped += char
    return swapped
