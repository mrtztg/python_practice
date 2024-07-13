def ch001_find_missing_number(nums):
    i, n = 0, len(nums)
    while i < n:
        destIdx = nums[i]
        if destIdx < n and nums[destIdx] != nums[i]:
            nums[i], nums[destIdx] = nums[destIdx], nums[i]
        else:
            i+=1

    for i in range(n):
        if i != nums[i]:
            return i
    return n