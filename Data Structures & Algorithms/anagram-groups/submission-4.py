class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        arr = [0] * 26
        count = {}
        for s in strs:
            for c in s:
                arr[ord(c)-ord('a')] += 1
            
            key = tuple(arr)
            if key not in count:
                count[key] = []
            count[key].append(s)
            arr = [0]*26

        return list(count.values())