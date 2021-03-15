def pascalLine(n):
    if (n==0):
        return [1]

    pre=pascalLine(n-1)
    cur=[]

    cur.append(1)    

    for i in range(len(pre)-1):
        cur.append(pre[i]+pre[i+1])
    cur.append(1)

    return cur
