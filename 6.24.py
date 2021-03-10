def names():
    students={}
    while True:
        n=input('Enter next name: ')
        if n=='':
            break
        if n in students:
            students[n]+=1
        else:
            students[n]=1
    for i in students:
        if students[i]==1:
            print('There is 1 student named ',i)
        else:
            print('There are ',students[i],' students named ',i)
names()
