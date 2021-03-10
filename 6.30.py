import random
def simul(n):
    counta=0
    countb=0
    for i in range(n):
        a=random.randrange(1,4)# 1 R 2 S 3 P
        b=random.randrange(1,4)
        if a==1 and b==2 or a==2 and b==3 or a==3 and b==1:
            counta+=1
        elif b==1 and a==2 or b==2 and a==3 or b==3 and a==1:
            countb+=1
    if counta>countb:
        print('Player 1')
    elif counta<countb:
        print('Player 2')
    else:
        print('Tie')
simul(eval(input()))        
