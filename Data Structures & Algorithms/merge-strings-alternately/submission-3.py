class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(len(word1)):
            if word1[i]:
                res += word1[i]
            if len(word2) > i:
                res += word2[i]

        if word2:
            res += word2[i+1:]

        return res