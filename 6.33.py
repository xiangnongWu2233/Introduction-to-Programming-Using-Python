import random
def diceprob(r):
    count=0
    times=0
    while count<100:
        times+=1
        x=random.randrange(2,13)
        if x==r:
            count+=1
    print('It took ',times,' rolls to get 100 rolls of ',r)
diceprob(eval(input()))
