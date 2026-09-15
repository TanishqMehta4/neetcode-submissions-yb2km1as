class StockSpanner:

    def __init__(self):
        self.s= []

    def next(self, price: int) -> int:
        span = 1
        while self.s and price >= self.s[-1][0]:
            oldprice,oldspan = self.s.pop()
            span += oldspan

        self.s.append([price,span])
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)