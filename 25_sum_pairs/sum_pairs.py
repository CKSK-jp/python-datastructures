def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) 
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([0,1,2,3,4,5,6,7,1,6], 7)
        (3, 4)
        
        [0,1,2,3,4,5,6,7,8,9]
        smallest_vals = [6, 7, 9]
        results = [(0, 6), (4, 7), (8, 9)]
        first_pair_i = results.index(min([6, 7, 9]))
        return results[first]

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    
    seen_values = set()

    for num in nums:
        target = goal - num
        if target in seen_values:
            return (target, num)
        seen_values.add(num)

    return ()

    # other_pairs = []
    # smallest_vals = []
    # new_array = nums
    # for i in range(len(nums) - 1):
    #     other_val = goal - nums[i]
    #     if other_val in new_array:
    #         new_array = nums[i + 1:nums.index(other_val):1]
    #         current_val = nums[i]
    #         smallest_vals.append(nums.index(other_val))
    #         other_pairs.append((current_val, other_val))
    #         if len(new_array) < i:
    #                 break
    # if len(smallest_vals) == 0:
    #     return ()
    # return other_pairs[smallest_vals.index(min(smallest_vals))]


            