from collections import deque
stack = deque()

class stack:
    def __init__(self):
        self.box=deque()
    
    def push(self,value):
        self.box.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def print(self):
        print(self.box)

if __name__=="__main__":
    a = stack()
    a.push(1)
    a.print()