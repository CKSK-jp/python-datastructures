def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    results = {}
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in phrase.lower():
        if char in vowels:
            results[char] = results.get(char, 0) + 1
    return results

    # return {char: phrase.lower().count(char) for char in vowels if char in phrase.lower()}
