def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    # list_of_words = phrase.split(' ')
    # capitalized = ''
    # for word in list_of_words:
    #     capitalized = capitalized + word[0].upper() + word[1::1].lower() + ' '
    # return capitalized.strip()
    
    
    capitalized = [word[0].upper() + word[1::1].lower() for word in phrase.split(' ')]
    return (' '.join(capitalized))
