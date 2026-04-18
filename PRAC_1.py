class MinStack:
    def __init__(self,n):
        self.s= []
        self.min=[]
        self.n = n
    def push(self,x):
        if len(self.s) == self.n: print("overflow")
        else:
            self.s.append(x)
            if not self.min or x <= self.min[-1]:
                self.min.append(x)
    def pop(self):
        if not self.s: print("underflow")
        else:
            x = self.s.pop()
            if x == self.min[-1]: self.min.pop()
    def display(self):
        print(self.s)
        print(self.min)
s = MinStack(5)
s.push(6)
s.push(3)
s.push(1)
s.push(9)
s.push(6)
s.pop()
s.display() 