class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxcount = 0
        for num in numSet:
            if num - 1 in numSet:
                continue
            else:
                count = 1
                while num + 1 in numSet:
                    num +=1 
                    count += 1
                maxcount = max(count,maxcount)


        return maxcount
                
