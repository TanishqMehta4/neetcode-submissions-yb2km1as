class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isalnum(c):
            if (ord("a") <= ord(c) <= ord("z")) or (ord("0") <= ord(c) <= ord("9")) or (ord("A") <= ord(c) <= ord("Z")):
                return True
            return False

        l,r = 0, len(s)-1
        while l <r:
            while l<r and not isalnum(s[l]):
                l+=1
            while l<r and not isalnum(s[r]):
                r-=1
            if l <r and s[l].lower() != s[r].lower():
                return False
            else:
                r-=1
                l+=1

        return True    
        
