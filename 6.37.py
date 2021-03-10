def zipf(file):
    text=open(file,'r')
    text=text.read()
    count=dict()
    table=str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ,.!?;:"\'`~-_$&@#%',
                        'abcdefghijklmnopqrstuvwxyz                 ')
    total=0
    text=text.translate(table)
    words=text.split()
    for i in words:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
        total+=1
    fre=[]
    for i in count:
        fre.append(count[i])
    fre.sort()
    for i in range(len(fre)-1,len(fre)-11,-1):
        print(fre[i]/total)
