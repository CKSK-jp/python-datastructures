def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    wordCount = {}
    for char in phrase:
        wordCount[char] = wordCount.get(char, 0) + 1
    return wordCount
    
print(f"Test Case 1: {multiple_letter_count('yay') == {'y': 2, 'a': 1}}")
print(f"Test Case 2: {multiple_letter_count('Yay') == {'Y': 1, 'a': 1, 'y': 1}}")