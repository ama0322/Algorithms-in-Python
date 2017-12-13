def first_two(str):
    """
    Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".


    first_two('Hello') → 'He'
    first_two('abcdefg') → 'ab'
    first_two('ab') → 'ab'
    """

    if len(str) < 2:
        return str
    else:
        return str[0:2]