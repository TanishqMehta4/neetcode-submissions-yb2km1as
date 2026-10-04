class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        l=0
        minWindow = float("inf")
        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                minWindow = min(r - l +1,minWindow)
                total -= nums[l]
                l+=1

        
        return 0 if minWindow == float("inf") else minWindow