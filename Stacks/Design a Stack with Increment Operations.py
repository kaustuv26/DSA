class CustomStack(object):

    def __init__(self, maxSize):
        self.stack = []
        self.maxSize = maxSize
        self.inc = []
        

    def push(self, x):
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc.append(0)
        

    def pop(self):
        if not self.stack:
            return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()
