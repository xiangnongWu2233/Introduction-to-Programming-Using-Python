import random
def craps():
    card1=random.randrange(1,7)
    card2=random.randrange(1,7)
    total=card1+card2
    if total == 7 or total == 11: return 1
    elif total == 2 or total == 3 or total == 12: return 0
    else:
        card1=random.randrange(1,7)
        card2=random.randrange(1,7)
        while card1+card2!=7 and card1+card2!=total:
            total=card1+card2
            card1=random.randrange(1,7)
            card2=random.randrange(1,7)
        if card1+card2==7: return 0
        else: return 1
