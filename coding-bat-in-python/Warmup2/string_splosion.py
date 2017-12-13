def string_splosion(str):
    """
    Given a non-empty string like "Code" return a string like "CCoCodCode".


    string_splosion('Code') → 'CCoCodCode'
    string_splosion('abc') → 'aababc'
    string_splosion('ab') → 'aab'
    """

    answer = ""

    for x in range(0, len(str)):
        answer += str[0: x+1]

    return answer
