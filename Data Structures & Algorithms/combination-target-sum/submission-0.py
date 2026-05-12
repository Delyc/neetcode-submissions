class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def gen(i, arr, summ):
            if summ == target:
                res.append(arr[:])
                return
            if summ > target:
                return
            if i >= len(nums):
                return

            arr.append(nums[i])
            gen(i, arr, summ + nums[i])
            arr.pop()
            gen(i + 1, arr, summ)    
            
        gen(0, [], 0)
        return res
            

        