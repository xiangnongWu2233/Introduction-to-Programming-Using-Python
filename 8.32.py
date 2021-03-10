import random
class Craps:
    dice=[1,2,3,4,5,6]
    def __init__(self):
        total=random.choice(Craps.dice)+random.choice(Craps.dice)
        self.point=total
        if total==7 or total==11:
            print('Throw total: %d. You won!' %total)
        elif total==2 or total==3 or total==12:
            print('Throw total: %d. You lost!' %total)
        else:
            print('Throw total: %d. Throw for Point.' %total)
    def forPoint(self):
        total=random.choice(Craps.dice)+random.choice(Craps.dice)
        if total==self.point:
            print('Throw total: %d. You won!' %total)
        elif total==7:
            print('Throw total: %d. You lost!' %total)
        else:
            print('Throw total: %d. Throw for Point.' %total)
        self.point=total
