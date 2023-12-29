def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    # solution 1
    # lst_str1, lst_str2 = str(num1), str(num2)
    # dict1, dict2 = {}, {}
    # for val in lst_str1:
    #     dict1[val] = dict1.get(val, 0) + 1
    # for val in lst_str2:
    #     dict2[val] = dict2.get(val, 0) + 1
    # return dict1.items() == dict2.items()

    # solution 2
    # list_num_1 = list(map(int,str(num1)))
    # list_num_2 = list(map(int,str(num2)))
    # if len(str(num1))!=len(str(num2)):
    #     return False
    # else:
    #     dict1 = {list_num_1[i]: list_num_1.count(i) for i in set(list_num_1)}
    #     dict2 = {list_num_2[i]: list_num_2.count(i) for i in set(list_num_2)}
    #     return dict1.items() == dict2.items()

    # solution 3
    return sorted(str(num1)) == sorted(str(num2))
