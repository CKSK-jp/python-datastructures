def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    days = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday',
    }
    answer = days.get(day_of_week)
    return answer
    
    
# tests
print(f"Test Case 1: {weekday_name(1) == 'Sunday'}")
print(f"Test Case 2: {weekday_name(7) == 'Saturday'}")
print(f"Test Case 3: {weekday_name(0) == None}")
print(f"Test Case 4: {weekday_name(9) == None}")

