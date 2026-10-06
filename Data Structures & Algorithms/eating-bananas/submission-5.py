class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 0,max(piles)

        def isValid(m):
            if m ==0:
                return False
            count = 0
            for pile in piles:
                count += -(-pile//m) 
            
            if count <= h:
                return True
            return False

        while l<=r:
            m = (l + r) // 2
            if isValid(m):
                r = m-1
            else:
                l = m+1
        
        return m if isValid(m) else m+1
