def string_bits(str):
    """
    Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


    string_bits('Hello') → 'Hlo'
    string_bits('Hi') → 'H'
    string_bits('Heeololeo') → 'Hello'
    """

    everyOther = ""

    for x in range(0, len(str), 2):
        everyOther += str[x]

    return everyOther
