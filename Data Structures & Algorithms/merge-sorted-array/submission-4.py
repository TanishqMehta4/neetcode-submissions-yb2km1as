class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        n = n-1
        m = m-1

    
        for last in range(len(nums1)-1,-1,-1):
            if n< 0:
                break

            elif m>=0 and nums1[m] >= nums2[n]:
                nums1[last] = nums1[m]
                m-=1
            else:
                nums1[last] = nums2[n]
                n-=1

        return nums1