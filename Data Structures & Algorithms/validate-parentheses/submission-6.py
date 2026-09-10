class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            "]":"[",
            ")":"(",
            "}":"{"
        }
        res = []

        for c in s:
            if c in closeToOpen:
                if res and closeToOpen[c] == res[-1]:
                    res.pop()
                else:
                    return False
            else:

                res.append(c)

        return len(res) == 0