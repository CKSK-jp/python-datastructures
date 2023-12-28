def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """

    factors = []
    counter = 1
    end = int(num / 2)
    while counter < end:
        if num % counter == 0:
            factors.append(counter)
            quo = int(num / counter)
            factors.append(quo)
            end = quo**0.5
        counter += 1
    factors.sort()
    return factors