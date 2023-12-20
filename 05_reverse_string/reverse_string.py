def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    # return phrase[::-1] also works where [0:1:-1]
    # 0 is the start to slice, 1 is the index where slice ends, -1 is the step size, to traverse reverse in this case
    return ''.join(list(reversed(phrase)))

print(f"Test Case 1: {reverse_string('awesome') == 'emosewa'}")
print(f"Test Case 2: {reverse_string('sauce') == 'ecuas'}")