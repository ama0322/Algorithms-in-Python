def sum3(nums):
    """
    Given an array of ints length 3, return the sum of all the elements.


    sum3([1, 2, 3]) → 6
    sum3([5, 11, 2]) → 18
    sum3([7, 0, 0]) → 7
    """

    sum = 0
    for x in range(len(nums)):
        sum += nums[x]

    return sum