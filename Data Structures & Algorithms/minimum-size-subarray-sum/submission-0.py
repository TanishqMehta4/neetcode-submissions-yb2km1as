class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float("inf")
        numsum = 0
        for r in range(len(nums)):
            numsum += nums[r]

            while numsum >= target:
                res = min(r - l + 1,res)
                numsum -= nums[l]
                l += 1


        return res if res != float("inf") else 0