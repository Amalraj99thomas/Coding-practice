class stackNode():
    def __init__(self, value):
        self.data = value 
        self.next = None

class MinStack():
    def __init__(self, value):
        self.top = None

    def push(self, value: int) -> None:
        new_node = stackNode(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top == None:
            return 'Empty Stack'
        else:
            data = self.top.data
            self.top = self.top.next
            return data

    def peek(self):
        if self.top == None:
            return 'Empty Stack'
        else:
            return self.top.data

    def getMin(self):

        # my thinking
        # temp = self.top

        # while temp != None:
        #     min = min(temp.data, temp.next.data)
        #     temp = temp.next
        # return min
    
        # # second implementation
        temp = self.top
        min = temp

        while temp != None:
            if temp.data < min.data:
                min = temp
            temp = temp.next
        return min.data
    

