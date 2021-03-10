def inValues():
    sum=0.0
    count=0
    while True:
        try:
            number=eval(input('Please enter a number: '))
            if number==0:
                return sum
            sum+=number
        except:
            if count==0:
                print('Error. Please re-enter the value.')
                count+=1
                continue
            else:
                print('Two errors in a row. Quitting ...')
                break
