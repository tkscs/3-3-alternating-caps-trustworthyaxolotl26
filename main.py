words = input("what is your message: ")

def alt_caps(original_string):
    x = 1
    """Convert a string to Alternating Caps

    Args:
        original_string (str): A given string with any kind of capitalization
    Returns:
        str: A new string with alternating capitalization
    Examples:
        >>> print(alt_caps("Alternating Capitalization"))
        aLtErNaTiNg CaPiTaLiZaTiOn
    """
    new_string = ""

    i = 0

    for character in words:
        if x > 0:
            words.upper
            character.upper
            new_string += words[i]
            i += 1
            x -= 1
        else:
           # words.lower
            new_string += character
            i += 1
            x += 1

    #new_string += words.upper()

    return new_string

print(alt_caps(words))

