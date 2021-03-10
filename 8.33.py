class Pseudorandom:
    def __init__(self,a,x,c,m):
        self.lst=[(a*x+c)%m]
        self.index=x
        self.a, self.x, self.c, self.m=a,x,c,m
    def next(self):
        item=(self.index*self.a+self.c)%self.m
        self.lst.append(item)
        self.index=item
        return item
