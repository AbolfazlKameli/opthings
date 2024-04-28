def twoSum(nums, target):
    p1 = 0
    p2 = len(nums) - 1
    while p1 < p2:
        s = nums[p1] + nums[p2]
        if s == target:
            return [p1 + 1, p2 + 1]
        elif s > target:
            p2 -= 1
        else:
            p1 += 1
