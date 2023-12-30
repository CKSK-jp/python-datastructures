def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    listed_s = list(s)
    vowels_found = [char for char in listed_s if char.lower() in vowels]
    vowels_found.reverse()
    for i, char in enumerate(listed_s):
        if char.lower() in vowels:
            listed_s[i] = vowels_found.pop(0)
    return ''.join(listed_s)