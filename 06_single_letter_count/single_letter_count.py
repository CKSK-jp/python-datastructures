def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    result = 0
    for char in word.lower():
        if char == letter:
            result += 1
    return result
    
print(f"Test Case 1: {single_letter_count('Hello World', 'h') == 1}")
print(f"Test Case 2: {single_letter_count('Hello World', 'z') == 0}")
print(f"Test Case 3: {single_letter_count('Hello World', 'l') == 3}")