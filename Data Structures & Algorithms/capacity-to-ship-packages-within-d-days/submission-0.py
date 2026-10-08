class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights),sum(weights)

        def isValid(cap):
            boat = 1
            count = 0
            for w in weights:
                count += w
                if count > cap:
                    count = w
                    boat+=1
                
                if boat>days:
                    return False
            
            return True

        while l<=r:
            m = (l+r)//2
            if isValid(m):
                r = m -1
            else:
                l = m+1

        return m if isValid(m) else m+1
