def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # results = []
    # for val in lst:
    #     results.append(True) if isinstance(val, list) else results.append(False)
    # return all(results)

    return all(isinstance(x,list) == True for x in lst)