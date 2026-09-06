class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0

        # Sum of the first window
        for i in range(k):
            total += nums[i]

        max_avg = total / k

        # Slide the window
        for i in range(len(nums) - k):
            total = total - nums[i] + nums[i + k]

            current_avg = total / k

            if current_avg > max_avg:
                max_avg = current_avg

        return max_avg