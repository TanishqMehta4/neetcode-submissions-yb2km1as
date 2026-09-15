class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        res = [0] * len(temperatures)

        for i,t in enumerate(temperatures):
            while temps and temps[-1][0] < t:
                temp,tempidx = temps.pop()
                res[tempidx] = i - tempidx
            
            
            temps.append([t,i])

        return res