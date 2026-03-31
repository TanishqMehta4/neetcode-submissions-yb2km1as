class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        l = 0

        while l < len(s):
            
            num = ""

            while s[l] != '#':
                num += s[l]
                l+=1  

            res.append(s[l+1 : l+int(num)+1])

            l += int(num) + 1

        return res