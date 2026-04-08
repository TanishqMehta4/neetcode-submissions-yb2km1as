class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0 ,len(height) - 1
        total = 0
        lmax = height[l]
        rmax = height[r]


        while l < r:
            
            
            if lmax <= rmax:
                l+=1

                lmax = max(height[l],lmax)
                total += lmax - height[l]

            else:
                r-=1
                rmax = max(height[r],rmax)

                total += rmax - height[r]
                

        return total