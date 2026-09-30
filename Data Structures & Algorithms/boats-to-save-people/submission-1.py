class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()

        l,r = 0,len(people) - 1

        while l<=r:
            remaining = limit - people[r]
            boats += 1
            r-=1

            if l<=r and remaining >= people[l]:
                l+=1
                
        return boats
        
        

