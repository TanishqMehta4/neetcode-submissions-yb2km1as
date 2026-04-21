class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)

        return max(count,key=count.get)
