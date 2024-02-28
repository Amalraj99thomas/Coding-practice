# create two stacks: 
# 1 for regular values
# 2 for keeping track of min value

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value):
        self.stack.append(value)
        # adding the min of value and minstack value to minstack
        value = min(value, self.minStack[-1] if self.minStack else value)
        self.minStack.append(value)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minStack[-1]