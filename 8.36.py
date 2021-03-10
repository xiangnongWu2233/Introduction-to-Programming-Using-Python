class PriorityQueue:
    def __init__(self):
        self.queue=[]
    def insert(self,item):
        self.queue.append(item)
        self.queue.sort()
    def min(self):
        return self.queue[0]
    def removeMin(self):
        self.queue.remove(self.queue[0])
    def isEmpty(self):
        if len(self.queue)==0:
            return True
        else:
            return False
    def __len__(self):
        return len(self.queue)
