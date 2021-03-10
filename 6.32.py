import random
def manhattan(length, width):
    ans=[]
    for i in range(length):
        ans.append([])
        for j in range(width):
            ans[i].append(0)
    x=int(length/2)
    y=int(width/2)
    while x>=0 and x<length and y>=0 and y<width:
        ans[x][y]+=1
        q=random.randrange(0,4)
        if q==0:
            x+=1
        if q==1:
            x-=1
        if q==2:
            y+=1
        if q==3:
            y-=1
    for i in range(length):
        print(ans[i])
