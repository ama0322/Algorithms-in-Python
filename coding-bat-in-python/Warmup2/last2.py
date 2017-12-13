def last2(str):
    """
    Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


    last2('hixxhi') → 1
    last2('xaxxaxaxx') → 1
    last2('axxxaaxx') → 2
    """

    last2 = str[-2: ]
    counter = 0

    # going up to the third to last digit
    for x in range(0, len(str) - 2):
        if last2 == str[x: x+2]:
            counter = counter+1

    return counter
