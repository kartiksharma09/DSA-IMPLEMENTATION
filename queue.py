############ QUEUE IMPLEMENTATION #########################

from collections import deque
queue = deque()

class queue:
    def __init__(self):
        self.buffer = deque()

    def peek(self):
        return self.buffer[-1]

    def push(self,value):
        self.buffer.appendleft(value)

    def pop(self):
        return self.buffer.pop()

    def is_empty(self):
        return self.buffer == []

    def length(self):
        return len(self.buffer)

    def show(self):
        print(self.buffer)

if __name__=="__main__":

    a=queue()
    a.push(1)
    print(a.length())
    a.show()
############################################################################ 