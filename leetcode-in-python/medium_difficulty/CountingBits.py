def Solution(num):
    """
    Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of
    1's in their binary representation and return them as an array.

    Example:
    For num = 5 you should return [0,1,1,2,1,2].

    Follow up:

    It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time
    O(n) /possibly in a single pass?

    Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any
    other language.

    :param num: input number to be processed
    :return: the answer
    """

    array = []

    for i in range(0, num + 1):

        bin_rep = str(bin(i))[2:]  # convert the number into a string form of the binary representation
        one_count = 0

        for x in range(len(bin_rep)):
            if bin_rep[x] == "1":
                one_count = one_count + 1

        array.append(one_count)  # add that number to the array

    return array
