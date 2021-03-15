def levy(n):
    if n==0:
        return 'F'
    pre=levy(n-1)
    now=''
    for i in range(len(pre)):
        if pre[i]=='F':
            now+='L'
            now+='F'
            now+='R'
            now+='F'
            now+='L'
        else:
            now+=pre[i]
    return now
            
