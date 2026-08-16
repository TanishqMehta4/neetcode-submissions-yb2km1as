class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        k %= n
        l = 0
        r = len(nums) - 1
        
        def reverse(l,r):
            while l<r:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1
            return nums

        nums = reverse(l,r)
        nums = reverse(l,k-1)
        nums = reverse(k,r)



            