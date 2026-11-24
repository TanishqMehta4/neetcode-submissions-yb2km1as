class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_len = len(cost)
        one = cost[cost_len-1]
        two = cost[cost_len-2]
        three = 0

        for i in range(cost_len -3,-1,-1):
            three = min(cost[i]+one,cost[i]+two)
            one = two
            two = three
        

        return min(one,two)

