class Stack(object):
    def __init__(self):
        self.stack=[]
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def isEmpty(self):
        if(len(self.stack)==0):
            return True
        else:
            return False
    def len(self):
        return len(self.stack)
