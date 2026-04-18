"""
Write a program for implementing a MINSTACK,
which should support operations like push, pop,
overflow, underflow, display
"""

class MinStack: 
    def __init__(self, n): 
        self.s = [] 
        self.min = [] 
        self.n = n 
    
    def push(self, x): 
        if len(self.s) == self.n: 
            print("Overflow")
        else: 
            self.s.append(x)
            if not self.min or x <= self.min[-1]: 
                self.min.append(x) 
    
    def pop(self): 
        if not self.s: 
            print("Underflow")
        else: 
            x = self.s.pop()
            if x == self.min[-1]:
                self.min.pop()
    def display(self): 
        print(self.s)
        

s = MinStack(5)
s.push(10)
s.push(5)
s.push(20)
s.display()
s.pop()
s.display()
