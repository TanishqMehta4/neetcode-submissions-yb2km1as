class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        countS = {}
        countT = {}

        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i],0)

        res = ""
        count = float("inf")
        l = 0
        have = 0
        need = len(countT)

        for r in range(len(s)):

            if s[r] in countT:
                countS[s[r]] = 1 + countS.get(s[r],0)
                if countS[s[r]] == countT[s[r]]:
                    have += 1

            while have == need:
                if r-l+1 < count:
                    res = s[l:r+1]
                    count = r-l+1
                
                if s[l] in countT:
                    countS[s[l]] -=1 
                    if countT[s[l]] > countS[s[l]]:
                        have -= 1

                l+=1

            
            
        return res