'''
V3 - this solution attempts a solve by using  a sliding window. However, this time, a dictionary is used to store
     values instead of a list. Two pointers are used in a sliding windows approach, similar to V2. The left pointer
     indicates the start of the substring, and the right pointer indicates the end. If the right pointer reaches a
     character that has already been seen, then move the left pointer one space forward.
'''
def Solution(s):
    """
    Given a string, find the length of the longest substring without repeating characters.

    Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a
        subsequence and not a substring.

    :type s: str - input string to be processed
    :rtype: int - length of the longest non-repeating string
    """

    # if the string is empty, return 0
    if len(s) == 0:
        return 0

    # dictionary that stores characters as the key and the index as the value
    unique_chars = {}

    max_len = 1
    l_pointer = 0

    for r_pointer in range(len(s)):

        current_char = s[r_pointer]
        if current_char in unique_chars:
            # update the l_pointer if the index for the original same character +1 is bigger
            l_pointer = max(l_pointer, unique_chars[current_char] + 1)

        # put in the current char with its index into the unique_chars dictionary
        unique_chars.update({current_char: r_pointer})

        # update the max_len based on the left and right pointers
        max_len = max(max_len, r_pointer - l_pointer + 1)

    return max_len


'''
V2(Fail) - this solution attempts to solve by taking every index and forming a sliding window extending to the end
           of the strings. If the new character added by incrementing the window by 1 is already seen, then I
           do not use that when considering a substring of maximum length. It works, but take too long.
def Solution(self, s):
    """
    Given a string, find the length of the longest substring without repeating characters.

    Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a
        subsequence and not a substring.

    :type s: str - input string to be processed
    :rtype: int - length of the longest non-repeating string
    """

    # if string is empty, return 0
    if s == "":
        return 0

    maxlen = 1
    ln = len(s)

    # go through every index in the string
    for sub_start in range(0, ln):

        unique_chars = [] # list containing unique chars, used to check the substrings
        unique_chars.append(s[sub_start]) # add the first character in the substring into the unique chars list
        continue_now = False  # boolean used to break into this loop from for loop sub_end in range...

        # use the sliding windows approach and slide the right side of the substring all the way to the end of s
        for sub_end in range(sub_start + 1, ln):

            sub = s[sub_start: sub_end + 1]
            new_char = s[sub_end] # character at index sub_end

            # if new_char is already in unique_chars, skip to the next sub_start loop iteration
            if new_char in unique_chars:
                continue_now = True
                break

            # otherwise, check the length of this current substring to the maxlen and add the char to unique_chars
            else:
                if len(sub) > maxlen:
                    maxlen = len(sub)
                unique_chars.append(new_char)

        if continue_now:
            continue

    return maxlen
'''

'''
V1(Fail): This brute force method, which checks all possible substrings, was not accepted because it is too slow
def Solution(self, s):
    """
    Given a string, find the length of the longest substring without repeating characters.

    Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

    :type s: str - input string to be processed
    :rtype: int - length of the longest non-repeating string
    """

    # if the string is empty, return 0
    if len(s) == 0:
        return 0


    maxlen = 1

    # go through every index(i) in the string, and process the substring formed by that and j
    for i in range(0, len(s)):
        for j in range(i+1, len(s)):

            sub = s[i: j+1]

            no_repeat = True

            # check that the substring does not have any repeating characters
            for x in range(0, len(sub)):
                for y in range(x+1, len(sub)):
                    if sub[x] == sub[y]:
                        no_repeat = False

            if not no_repeat:
                continue

            # check if this sub is the largest registered substring
            if len(sub) >= maxlen:
                maxlen = len(sub)

    return maxlen
    
'''
