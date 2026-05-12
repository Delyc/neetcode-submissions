class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def gen(start, curr, summ):
            if summ == target:
                res.append(curr[:])
                return
            if summ > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[ i - 1]:
                    continue
                curr.append(candidates[i])
                gen(i + 1, curr, summ + candidates[i])
                curr.pop()
        
        gen(0, [], 0)
        return res
        