def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    freq = {}
    for val in lst:
        freq[val] = freq.get(val, 0) + 1
    return freq.get(search_term, 0)