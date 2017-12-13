def array_count9(nums):
    """
    Given an array of ints, return the number of 9's in the array.


    array_count9([1, 2, 9]) → 1
    array_count9([1, 9, 9]) → 2
    array_count9([1, 9, 9, 3, 9]) → 3
    """

    count = 0

    """
    regular for loop
    
    for x in range(0, len(nums)):
        if nums[x] == 9:
            count = count + 1
    """


    for x in nums:
        if x == 9:
            count = count+1

    return count