class Solution:
    def trap(self, height: List[int]) -> int:
        lmax,rmax,l,r = 0,0,0,len(height) - 1
        water = 0

        while l<=r:
            
            if lmax <= rmax:
                lmax = max(lmax,height[l])

                area = min(lmax,rmax) - height[l]
                if area > 0:
                    water += area
                l+=1

            else:
                rmax = max(rmax,height[r])

                area = min(lmax,rmax) - height[r]
                if area > 0:
                    water += area
                r-=1

        return water