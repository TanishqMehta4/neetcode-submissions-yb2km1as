class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l,r = 0,0
        count = 0

        while r <  len(s):

            while r<len(s) and s[r] not in seen: 
                seen.add(s[r])
                count = max(count, r-l+1)
                r+=1
            else:
                seen.remove(s[l])
                l+=1
                



        return count
