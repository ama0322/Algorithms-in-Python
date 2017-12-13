def has23(nums):
    """
    Given an int array length 2, return True if it contains a 2 or a 3.


    has23([2, 5]) → True
    has23([4, 3]) → True
    has23([4, 5]) → False
    """

    has23 = False

    for x in range(0, len(nums)):
        if nums[x] == 2 or nums[x] == 3:
            has23 = True

    return has23