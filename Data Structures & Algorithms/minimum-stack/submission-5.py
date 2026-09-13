class MinStack:

    def __init__(self):
        self.s = []
        self.min = float("inf")

    def push(self, val: int) -> None:
        self.min = min(self.s[-1][1],val) if self.s else val
        self.s.append([val,self.min]) 

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]
        
