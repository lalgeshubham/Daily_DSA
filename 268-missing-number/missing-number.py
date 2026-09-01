class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        for i in range(n - 1):
            diff = nums[i + 1] - nums[i]

            if diff > 1:
                return nums[i] + 1

        if nums[0] != 0:
            return 0

        return n       
