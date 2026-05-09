class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        p = float('-inf')
        idx = 0
        for i in range(len(nums)):
            left = nums[i - 1] if i - 1 > -1 else float('-inf')
            right = nums[i + 1] if i + 1 < len(nums) else float('-inf')

            if nums[i] > left and nums[i] > right:
                if nums[i] > p:
                    p = nums[i]
                    idx = i
        return idx
        