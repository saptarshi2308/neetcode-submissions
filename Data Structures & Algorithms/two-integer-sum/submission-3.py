class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevRes = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevRes:
                return [prevRes[diff], i]
            prevRes[n] = i
        return 
                
        