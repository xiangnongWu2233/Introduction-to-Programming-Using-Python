def coins(n):

    if(n<8):
        return False
    if(n==8):
        return True

    result=False
    
    if n%10==0:
        if coins(n-9)==True:
            return True
    if n%2==0:
        if coins(int(n/2)+1)==True:
            return True
    if n%3==0:
        if coins(n-7)==True:
            return True
    if n%4==0:
        if coins(n-6)==True:
            return True
    return False
