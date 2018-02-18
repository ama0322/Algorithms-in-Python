def Solution(nums, target):
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

    :type nums: List[int] - the list I'm working with
    :type target: int - target for the indices
    :rtype: List[int] - list ocntaining the indices
    """

    indices = []

    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                indices = [i, j]

    return indices
