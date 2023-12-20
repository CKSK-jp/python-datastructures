def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    # return phrase[::-1] also works where [x:y:z]
    # x is the start to slice, y is the index where slice ends, z is the step size, to traverse reverse in this case
    return ''.join(list(reversed(phrase)))


print(f"Test Case 1: {reverse_string('awesome') == 'emosewa'}")
print(f"Test Case 2: {reverse_string('sauce') == 'ecuas'}")