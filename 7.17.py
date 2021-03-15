import random
def game(n):
    count=0
    for i in range(n):
        a=random.randrange(0,10)
        b=random.randrange(0,10)
        print(a,' + ',b,' = ')
        try:
            x=eval(input('Enter answer: '))
            if a+b==x:
                print('Correct.')
                count+=1
            else:
                print('Incorrect.')
        except:
            print('Please enter answer using 0-9. Try again!')
            x=eval(input('Enter answer: '))
            if a+b==x:
                print('Correct.')
                count+=1
            else:
                print('Incorrect.')
    if count==1:
        print('You got 1 correct answer out of ',n) 
    else:
        print('You got ',count,' correct answers out of ',n)
